from flask import Flask,request
import datetime
import numpy

def all_routes(app):

    @app.route('/',methods=['GET'])
    def get_seconds():

        try:
            start_time = request.args.get('start_time')    # expecting times to be in ISO-8601 format
            end_time = request.args.get('end_time')

            if start_time == end_time :
                return str(0)


            start_date_time_obj = datetime.datetime.strptime(start_time.replace('T',' '), '%Y-%m-%d %H:%M:%S')
            end_date_time_obj = datetime.datetime.strptime(end_time.replace('T',' '), '%Y-%m-%d %H:%M:%S')

            start_hour = start_date_time_obj.hour
            start_minute = start_date_time_obj.minute
            start_second = start_date_time_obj.second

            end_hour = end_date_time_obj.hour
            end_minute = end_date_time_obj.minute
            end_second = end_date_time_obj.second


            all_p_holidays = [] # get holidays of all years between start and end
            for yr in range(start_date_time_obj.year,end_date_time_obj.year+1):
                all_p_holidays.extend([str(yr)+'-01-01', str(yr)+'-03-21', str(yr)+'-04-10', str(yr)+'-04-13', str(yr)+'-04-27', str(yr)+'-05-01', str(yr)+'-06-16', str(yr)+'-08-09', str(yr)+'-09-10', str(yr)+'-09-24', str(yr)+'-12-16', str(yr)+'-12-25', str(yr)+'-12-26'])


            s = datetime.date(start_date_time_obj.year,start_date_time_obj.month,start_date_time_obj.day )
            e = datetime.date(end_date_time_obj.year,end_date_time_obj.month,end_date_time_obj.day)
            bd_cal = numpy.busdaycalendar(holidays=all_p_holidays)
            all_days  = numpy.busday_count(s, e, busdaycal=bd_cal)


            if  start_hour < 8:
                start_hour = 00
                start_minute = 00
                start_second = 00


            if start_hour >= 17 :
                current_day = str(start_date_time_obj.year)+'-'+ (str(start_date_time_obj.month) if start_date_time_obj.month>=10 else "0"+str(start_date_time_obj.month)) +'-'+ (str(start_date_time_obj.day) if start_date_time_obj.day>=10 else "0"+str(start_date_time_obj.day))
                if current_day not in all_p_holidays or start_date_time_obj.weekday!=5 or start_date_time_obj!=6:
                    all_days = all_days - 1
                    start_hour = 00
                    start_minute = 00
                    start_second = 00


            if  start_hour >=8  and  start_hour <17:
                start_hour = 17 - start_hour


            if end_hour < 8 :
                end_hour = 00

            if end_hour <= 17 and end_hour >8 :
                end_hour =  end_hour - 8



            start_time_bussiness = datetime.timedelta(days=0,hours=start_hour, minutes=start_minute,seconds=start_second)
            end_time_bussiness = datetime.timedelta(days=0,hours=end_hour, minutes=end_minute,seconds=end_second)
            all_time_bussiness = start_time_bussiness + end_time_bussiness

            

            days_to_hours = all_days * 8
            hours_to_seconds = days_to_hours * 60 * 60
            final_output =  int(hours_to_seconds + all_time_bussiness.total_seconds())

            return str(final_output)

        except Exception as e:
            return(str(e))

    @app.errorhandler(404)
    def route_route(error):
        return "Incorrect route!",404


# http://localhost:5000/?start_time=2020-03-22T16:30:03&end_time=2020-03-27T09:40:59
