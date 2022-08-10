from django.shortcuts import render
from datetime import datetime
from django.views import View
# Create your views here.


class attendanceView(View):
    """
        This class is for showing the details of attendance of all users after inserting .dat files.
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'list_attendance.html')

    def post(self, request, **kwargs):
        id = request.POST['id']
        try:
            file_name = request.FILES['datafile']
            file = file_name.readlines()
        except:
            return render(request, 'list_attendance.html')
        result = []
        for item in file:
            data = {}
            all_data = (str(item)).replace("b\'", '')
            all_data = all_data.replace('\\t', ' ')
            all_data = all_data.replace('\\r', '')
            all_data = all_data.replace('\\n', '')
            all_data = (str(all_data)).split(' ')
            lst = []
            for i in all_data:
                if i != "":
                    lst.append(i)
            all_data = lst
            all_data[2] = datetime.strptime(all_data[2], '%H:%M:%S')
            value = 0
            for item in result:
                if all_data[0] == item['id'] and all_data[1] == item['date']:
                    if all_data[2]:
                        item['checkout'] = all_data[2]
                        if 'checkin' in item:
                            item['duration'] = item['checkout']-item['checkin']
                    value = 1
                    break
            if value == 0:
                data['id'] = all_data[0]
                if (all_data[2].time()).strftime("%p") == "PM":
                    data['checkout'] = all_data[2]
                else:
                    data['checkin'] = all_data[2]
                data['date'] = all_data[1]
                result.append(data)
        if id:
            result_id = []
            for item in result:
                if item['id'] == id:
                    result_id.append(item)
            context = {
                'result': result_id
            }
        else:
            context = {
                'result': result
            }
        return render(request, 'list_attendance.html', context)
