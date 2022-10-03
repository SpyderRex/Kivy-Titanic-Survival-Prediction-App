import kivy
from kivymd.app import MDApp
from kivy.uix.carousel import Carousel
from kivy.core.audio import SoundLoader
import pickle

kivy.require('2.0.0')

class MyCarousel(Carousel):
    
    def model_checkbox_click(self, instance, value):
        if self.ids.decision_tree_model.active == True:
            self.model = 1
            self.ids.model_label.text = "Decision Tree Classifier"
        elif self.ids.sgd_model.active == True:
            self.model = 2
            self.ids.model_label.text = "Stochastic Gradient Descent"
        elif self.ids.random_forest_model.active == True:
            self.model = 3
            self.ids.model_label.text = "Random Forest Classifier"
        elif self.ids.log_reg_model.active == True:
            self.model = 4
            self.ids.model_label.text = "Logistic Regression"
        elif self.ids.knn_model.active == True:
            self.model = 5
            self.ids.model_label.text = "K Nearest Neighbors Classifier" 
        elif self.ids.gnb_model.active == True:
            self.model = 6
            self.ids.model_label.text = "Gaussian Naive Bayes"
        elif self.ids.perceptron_model.active == True:
            self.model = 7
            self.ids.model_label.text = "Perceptron"
        return self.model
        
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
        return int(self.age)
        
    def sibsp_slider_select(self, instance, value):
        self.sibsp = self.ids.sibsp_value.value
        self.ids.sibsp_label.text = str(int(self.sibsp))
        return int(self.sibsp)
        
    def parch_slider_select(self, instance, value):
        self.parch = self.ids.parch_value.value
        self.ids.parch_label.text = str(int(self.parch))
        return int(self.parch)
        
    def fare_slider_select(self, instance, value):
        self.fare = self.ids.fare_value.value
        self.ids.fare_label.text = str(self.fare)
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
        
        if self.model == 1:
            with open("pickle/decision_tree.pkl", "rb") as f:    
                mp = pickle.load(f)
        elif self.model == 2:
            with open("pickle/sgd.pkl", "rb") as f:    
                mp = pickle.load(f) 
        elif self.model == 3:
            with open("pickle/random_forest.pkl", "rb") as f:    
                mp = pickle.load(f)
        elif self.model == 4:
            with open("pickle/log_reg.pkl", "rb") as f:    
                mp = pickle.load(f)
        elif self.model == 5:
            with open("pickle/knn.pkl", "rb") as f:    
                mp = pickle.load(f)
        elif self.model == 6:
            with open("pickle/gnb.pkl", "rb") as f:    
                mp = pickle.load(f) 
        elif self.model == 7:
            with open("pickle/perceptron.pkl", "rb") as f:    
                mp = pickle.load(f) 
           
        prediction = mp.predict([[self.class_value, self.sex, self.age, self.sibsp, self.parch, self.fare, self.embark]])
        
        if prediction == [0]:
            self.ids.prediction_label.text = "Sorry, your passenger did not survive."
            sound = SoundLoader.load("sounds/sad.wav")
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
