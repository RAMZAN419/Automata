class DFA:

 def q0(input_String):
 
  if input_String=="0":
   c_state="q1"
  elif input_String=="1":
   c_state="q3"

  return c_state
  
 def q1(input_String):

  if input_String=="0":
   c_state="q0"
  elif input_String=="1":
   c_state="q2"
  return c_state

 def q2(input_String):

  if input_String=="0":
   c_state="q3"

  elif input_String=="1":
   c_state="q1"
  return c_state

 def q3(input_String):
 
  if input_String=="0":
   c_state="q2"
  elif input_String=="1":
   c_state="q0"
  return c_state
 
 def start(input_String,current_state):
  size=len(input_String)
  c_state=current_state
 
  for i in range(size):
   if c_state=="q0":
    c_state=self.q0(input_String[i])
 
   elif c_state=="q1":
    c_state=self.q1(input_String[i])
  
  
   elif c_state=="q2":
    c_state=self.q2(input_String[i])

   elif c_state=="q3":
    c_state=self.q3(input_String[i])

  return c_state  


if _name_ == "_main_" :
 dfa=DFA
 states=["q0","q1","q2","q3"]
 start_state="q0"
 final_state=["q0"]
 input_String=input("Enter a string ")
 current_state="q0"
 
 current_state= dfa.start(input_String, start_state)
 
 for i in final_state:
  if(current_state==i):
   print("Accepted ==",current_state)
  else:
   print("String Rejected ",current_state)
