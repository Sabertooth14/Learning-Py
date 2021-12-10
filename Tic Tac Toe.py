#!/usr/bin/env python
# coding: utf-8

# TIc TAc TOe game 

# In[12]:


#displayiing the board
print("Welcome to my Tic Tac Toe Game")
def display_board(game_board):
    print(board[7]+ "|" +board[8]+ "|" +board[9])
    print('------')
    print(board[4]+ "|" +board[5]+ "|" +board[6])
    print('------')
    print(board[1]+ "|" +board[2]+ "|" +board[3])
    


# In[13]:


board=[" "]*10
display_board(board)


# In[14]:


#taking input from the user

def user_input():
    position= 99
    while(position<0 or position>9):
            position= int(input("Enter a number between 0-9: "))
            print (position) 
            if position<0 or position>9:
                print("Wrong input.. Please try again")
                position= int(input("Enter a number between 0-9: ")) 
                if position>0 or position<9:
                    return position
            else:
                return position
        
                


# In[15]:


user_input()


# In[16]:


def user_choice():
    choice= input("chose X or O: ")
    print (choice)
    if choice!='X' and choice!='O':
        print("Wrong Choice")
        user_choice()
    else:
        return choice
    
    


# In[17]:


user_choice()


# In[18]:


def update():
    def user_choice():
        choice= input("choose X or O: ")
        if choice!='X' and choice!='O':
            print("Wrong Choice")
            user_choice()
        else:
            return choice
    while True:
        tp=user_choice()    
        result=user_input()
        board[result]=tp
        display_board(board)
        check_winner()


# In[19]:


update()
    


# In[20]:


def winner():
    update()


# In[ ]:


winner()


# In[23]:


def check_winner():
    if(board[1]==board[2]==board[3]):
        print("Youe have won")
    elif(board[1]==board[4]==board[7]):
        print("You have won")
    elif(board[1]==board[5]==board[9]):
        print("You have won")
    elif(board[2]==board[5]==board[8]):
        print("You have won")
    elif(board[3]==board[6]==board[9]):
        print("You have won")
    elif(board[3]==board[5]==board[7]):
        print("You have won")
    elif(board[4]==board[5]==board[6]):
        print("You have won")
    elif(board[7]==board[8]==board[9]):
        print("You have won")


# In[24]:


winner()


# In[25]:


winner()


# In[ ]:




