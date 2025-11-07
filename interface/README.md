Interface
    - usually if a function doesnt exist inside child class then we look at the parent class BUT
     in INTERFACE if the parent class has a function then the child class should also have that particular function 
     
     eg:
     interface Animal{
         const int EYES = 2
         function noise() -> str {}
     }
     
     class Dog implements Animal{
         int legs = 0
         str voice = "
         
         constructor (int l, str v){
             this.legs =1
             this.voice = v
         }
         
         function walk () -> str {
             return 'run'
         }
     }
     
     Throws error cuz Animal had function noise but Class Dog dont have it. to make it work class Dog should also have function noise()