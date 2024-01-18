from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import uniqueid
from kivy.network.urlrequest import UrlRequest
import json
from datetime import datetime
from layout import LoginScreen, RegisterScreen
from employeeScreen import EmployeeScreen

# class AttendanceApp(App):
#     def build(self):
#         self.sm = ScreenManager()

#         login_screen = LoginScreen(name='login')
#         register_screen = RegisterScreen(name='register')
#         employee_screen = EmployeeScreen(name='employee')

#         self.sm.add_widget(login_screen)
#         self.sm.add_widget(register_screen)
#         self.sm.add_widget(employee_screen)

#         return self.sm




class AttendanceApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=5)

        self.label = Label(text='Employee ID:')
        self.layout.add_widget(self.label)

        # Display the device's unique ID (MAC address in this case)
        self.device_id_label = Label(text=f'Device ID: {uniqueid.id}')
        self.layout.add_widget(self.device_id_label)

        # Start periodic checking
        Clock.schedule_interval(self.check_network, 5)

        return self.layout

    def check_network(self, dt):
        # Check network status periodically
        is_connected = self.is_connected_to_network()
        if is_connected:
            # The device is connected to a network, let's log attendance
            employee_id = self.label.text  # Use the employee ID entered in the app
            device_id = uniqueid.id
            timestamp = datetime.now().isoformat()

            url = 'http://127.0.0.1:5000/log-attendance'
            data = {'employee_id': employee_id, 'device_id': device_id, 'timestamp': timestamp}

            headers = {'Content-Type': 'application/json'}

            UrlRequest(url, req_body=json.dumps(data), req_headers=headers, on_success=self.on_success, on_failure=self.on_failure, method='POST')

    def is_connected_to_network(self):
        # You can implement your logic here to check if the device is connected to a network.
        # For simplicity, let's assume it's always connected in this example.
        return True

    def on_success(self, req, result):
        print(result)
        print('Attendance logged successfully.')

    def on_failure(self, req, result):
        print(f'Error logging attendance: {result}')

if __name__ == '__main__':
    AttendanceApp().run()
