from kivymd.app import MDApp
from kivy.uix.carousel import Carousel
from kivy.core.audio import SoundLoader
import pickle

class MyCarousel(Carousel):
    
    
    def class_checkbox_click(self, instance, value):
        if self.ids.first_class.active == True:
            self.class_value = 1
            self.ids.class_label.text = "First Class"
        elif self.ids.second_class.active == True:
            self.class_value = 2
            self.ids.class_label.text = "Second Class"
        elif self.ids.third_class.active == True:
            self.class_value = 3
            self.ids.class_label.text = "Third class"
        return (self.class_value)
        
    def sex_toggle(self, instance, state):
        if self.ids.female.state == "down":
            self.sex = 0
            self.ids.sex_label.text = "Female"
        elif self.ids.male.state == "down":
            self.sex = 1
            self.ids.sex_label.text = "Male"
        return self.sex
            
    def age_slider_select(self, instance, value):
        self.age = self.ids.age_value.value
        self.ids.age_label.text = str(int(self.age))
        print(int(self.age))
        return int(self.age)
        
    def sibsp_slider_select(self, instance, value):
        self.sibsp = self.ids.sibsp_value.value
        self.ids.sibsp_label.text = str(int(self.sibsp))
        print(int(self.sibsp))
        return int(self.sibsp)
        
    def parch_slider_select(self, instance, value):
        self.parch = self.ids.parch_value.value
        self.ids.parch_label.text = str(int(self.parch))
        print(int(self.parch))
        return int(self.parch)
        
    def fare_slider_select(self, instance, value):
        self.fare = self.ids.fare_value.value
        self.ids.fare_label.text = str(self.fare)
        print(float(self.fare))
        return float(self.fare)
        
    def embark_checkbox_click(self, instance, value):
        if self.ids.cherbourg.active == True:
            self.embark = 0
            self.ids.embark_label.text = "Cherbourg"
        elif self.ids.queenstown.active == True:
            self.embark = 1
            self.ids.embark_label.text = "Queenstown"
        elif self.ids.southampton.active == True:
            self.embark = 2
            self.ids.embark_label.text = "Southampton"
        return self.embark

    def predict_survival(self):
        
        with open("log_reg.pkl", "rb") as f:    
            model = pickle.load(f)
            
        prediction = model.predict([[self.class_value, self.sex, self.age, self.sibsp, self.parch, self.fare, self.embark]])
        
        if prediction == [0]:
            self.ids.prediction_label.text = "Sorry, your passenger did not survive."
            sound =SoundLoader.load("sounds/sad.wav")
            sound.play()
        elif prediction == [1]:
            self.ids.prediction_label.text = "Congratulations! Your passenger survived!"
            sound = SoundLoader.load("sounds/happy.wav")
            sound.play()
            
        return prediction
        
    
        

class TitanicSurvivalPredictionApp(MDApp):
    
    def build(self):
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        
        return MyCarousel()
        
        
if __name__ == "__main__":
    TitanicSurvivalPredictionApp().run()