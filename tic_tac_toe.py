from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class TicTacToe(App):
    def build(self):
        # Create a box layout for the entire screen
        screen_box_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Create global variables
        self.user2_name = ""
        self.user1_name = ""
        self.user_number = 0
        self.buttons_arr = [[None]*3 for _ in range(3)]  # Initializing a 2D array
        
        # Create a box layout for the text inputs
        text_boxLayout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        
        # Create text input for the first user
        firstuser_label = Label(text="Enter name of first user")
        self.first_user = TextInput(multiline=False, font_size=20)
        text_boxLayout.add_widget(firstuser_label)
        text_boxLayout.add_widget(self.first_user)
        
        # Create text input for the second user
        seconduser_label = Label(text="Enter name of second user")
        self.second_user = TextInput(multiline=False, font_size=20)
        text_boxLayout.add_widget(seconduser_label)
        text_boxLayout.add_widget(self.second_user)
        screen_box_layout.add_widget(text_boxLayout)
        
        # Bind the text inputs
        self.first_user.bind(text=self.name_entered_1)
        self.second_user.bind(text=self.name_entered_2)
        
        # Create a grid layout for the tic-tac-toe board
        tic_tac_toe_grid = GridLayout(cols=3, rows=3, spacing=5)
        
        # Create buttons for the tic-tac-toe board
        for row in range(3):
            for column in range(3):
                ticTacToe_buttons = Button(font_size="20sp", background_color=(0.2, 0.2, 0.2, 1), color=(1, 1, 1, 1))
                self.buttons_arr[row][column] = ticTacToe_buttons
                ticTacToe_buttons.bind(on_press=self.button_clicked)
                tic_tac_toe_grid.add_widget(ticTacToe_buttons)
        
        screen_box_layout.add_widget(tic_tac_toe_grid)
        
        # Create update textinput
        self.update = TextInput(font_size=20, readonly=True, width=50)
        screen_box_layout.add_widget(self.update)
        
        return screen_box_layout

    def button_clicked(self, instance):
        #Check if user names are entered
        if not self.user1_name or not self.user2_name:
            self.update.text = "Please enter both user names first."
            return
        #Check user number
        self.user_number += 1
        if self.user_number % 2 == 0:
            instance.text = "X"
            self.update.text = f"It is now {self.user1_name}'s turn"
        else:
            instance.text = "O"
            self.update.text = f"It is now {self.user2_name}'s turn"
        #Disable the clicked button
        instance.disabled = True
        #Check if the game has been won
        self.ticTacToe_condition()

    def name_entered_1(self, instance, value):
        #Assign name of first user
        self.user1_name = value
        #Check if game can be started
        if self.user1_name and self.user2_name:
            self.update.text="You can now start the game by clicking on the buttons"

    def name_entered_2(self, instance, value):
        #Assign name of second user
        self.user2_name = value
        #Check if game can be started
        if self.user1_name and self.user2_name:
            self.update.text="You can now start the game by clicking on the buttons"

    def ticTacToe_condition(self):
        # Check rows and columns for a win
        for i in range(3):
            if self.buttons_arr[i][0].text == self.buttons_arr[i][1].text == self.buttons_arr[i][2].text and self.buttons_arr[i][0].text != "":
                self.win()
                self.finish_game()
                break
            if self.buttons_arr[0][i].text == self.buttons_arr[1][i].text == self.buttons_arr[2][i].text and self.buttons_arr[0][i].text != "":
                self.win()
                self.finish_game()
                break
        # Check diagonals for a win
        if self.buttons_arr[0][0].text == self.buttons_arr[1][1].text == self.buttons_arr[2][2].text and self.buttons_arr[0][0].text != "":
            self.win()
            self.finish_game()
        elif self.buttons_arr[0][2].text == self.buttons_arr[1][1].text == self.buttons_arr[2][0].text and self.buttons_arr[0][2].text != "":
            self.win()
            self.finish_game()
        # Check for a draw
        if self.user_number == 9:
            self.update.text = "It's a draw! The game has finished!"
            self.finish_game()

    def win(self):
        #Check which user has won the game
        if self.user_number % 2 == 0:
            self.update.text = f"Congrats, {self.user2_name}, you have won the game"
            #Restart the game
            self.finish_game()
        else:
            self.update.text = f"Congrats, {self.user1_name}, you have won the game"
            #Restart the game
            self.finish_game()
    
    def finish_game(self):
        #Clear the buttons
        for row in range(3):
            for column in range(3):
                self.buttons_arr[row][column].text = ""
                #Enable buttons
                self.buttons_arr[row][column].disabled = False
                print(f"Button at {row} {column} = {self.buttons_arr[row][column].disabled}")
        #Clear the text inputs
        self.first_user.text = ""
        self.second_user.text = ""
        self.user2_name = ""
        self.user1_name = ""

if __name__ == '__main__':
    app = TicTacToe()
    app.run()
