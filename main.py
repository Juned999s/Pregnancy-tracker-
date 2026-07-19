from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import db

class HomeScreen(Screen):
    pass


class MedsScreen(Screen):
    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        container = self.ids.meds_list
        container.clear_widgets()
        for med in db.get_medicines():
            row = BoxLayout(size_hint_y=None, height=60, spacing=10)
            status = "Taken" if med[4] else "Pending"
            row.add_widget(Label(text=f"{med[1]} - {med[2]} @ {med[3]} [{status}]"))
            take_btn = Button(text="Mark Taken", size_hint_x=0.4)
            take_btn.bind(on_press=lambda inst, mid=med[0]: self.mark_taken(mid))
            del_btn = Button(text="Delete", size_hint_x=0.3)
            del_btn.bind(on_press=lambda inst, mid=med[0]: self.delete_med(mid))
            row.add_widget(take_btn)
            row.add_widget(del_btn)
            container.add_widget(row)

    def mark_taken(self, mid):
        db.mark_medicine_taken(mid)
        self.refresh()

    def delete_med(self, mid):
        db.delete_medicine(mid)
        self.refresh()

    def add_medicine(self):
        name = self.ids.med_name.text.strip()
        dose = self.ids.med_dose.text.strip()
        time_str = self.ids.med_time.text.strip()
        if name:
            db.add_medicine(name, dose, time_str)
            self.ids.med_name.text = ""
            self.ids.med_dose.text = ""
            self.ids.med_time.text = ""
            self.refresh()


class TestsScreen(Screen):
    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        container = self.ids.tests_list
        container.clear_widgets()
        for t in db.get_tests():
            row = BoxLayout(size_hint_y=None, height=60, spacing=10)
            row.add_widget(Label(text=f"{t[1]} | {t[2]} | {t[3]}"))
            del_btn = Button(text="Delete", size_hint_x=0.3)
            del_btn.bind(on_press=lambda inst, tid=t[0]: self.delete_test(tid))
            row.add_widget(del_btn)
            container.add_widget(row)

    def delete_test(self, tid):
        db.delete_test(tid)
        self.refresh()

    def add_test(self):
        name = self.ids.test_name.text.strip()
        date = self.ids.test_date.text.strip()
        result = self.ids.test_result.text.strip()
        if name:
            db.add_test(name, date, result)
            self.ids.test_name.text = ""
            self.ids.test_date.text = ""
            self.ids.test_result.text = ""
            self.refresh()


class AppointmentsScreen(Screen):
    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        container = self.ids.appts_list
        container.clear_widgets()
        for a in db.get_appointments():
            row = BoxLayout(size_hint_y=None, height=60, spacing=10)
            row.add_widget(Label(text=f"{a[1]} | Dr. {a[2]} | {a[3]}"))
            del_btn = Button(text="Delete", size_hint_x=0.3)
            del_btn.bind(on_press=lambda inst, aid=a[0]: self.delete_appt(aid))
            row.add_widget(del_btn)
            container.add_widget(row)

    def delete_appt(self, aid):
        db.delete_appointment(aid)
        self.refresh()

    def add_appointment(self):
        date = self.ids.appt_date.text.strip()
        doctor = self.ids.appt_doctor.text.strip()
        notes = self.ids.appt_notes.text.strip()
        if date:
            db.add_appointment(date, doctor, notes)
            self.ids.appt_date.text = ""
            self.ids.appt_doctor.text = ""
            self.ids.appt_notes.text = ""
            self.refresh()


class LogsScreen(Screen):
    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        container = self.ids.logs_list
        container.clear_widgets()
        for l in db.get_logs():
            row = BoxLayout(size_hint_y=None, height=60, spacing=10)
            row.add_widget(Label(text=f"{l[1]} | Weight: {l[2]}kg | Kicks: {l[3]} | {l[4]}"))
            del_btn = Button(text="Delete", size_hint_x=0.3)
            del_btn.bind(on_press=lambda inst, lid=l[0]: self.delete_log(lid))
            row.add_widget(del_btn)
            container.add_widget(row)

    def delete_log(self, lid):
        db.delete_log(lid)
        self.refresh()

    def add_log(self):
        date = self.ids.log_date.text.strip()
        weight = self.ids.log_weight.text.strip()
        kicks = self.ids.log_kicks.text.strip()
        symptoms = self.ids.log_symptoms.text.strip()
        if date:
            db.add_log(date, weight, kicks, symptoms)
            self.ids.log_date.text = ""
            self.ids.log_weight.text = ""
            self.ids.log_kicks.text = ""
            self.ids.log_symptoms.text = ""
            self.refresh()


class PregnancyTrackerApp(App):
    def build(self):
        db.init_db()
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(MedsScreen(name="meds"))
        sm.add_widget(TestsScreen(name="tests"))
        sm.add_widget(AppointmentsScreen(name="appointments"))
        sm.add_widget(LogsScreen(name="logs"))
        return sm

    def switch_to(self, screen_name):
        self.root.current = screen_name


if __name__ == "__main__":
    PregnancyTrackerApp().run()
