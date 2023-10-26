# 2-key-value-store-server-with-Balance-Loader
Created 2 key-value store servers with a load balancer that can be accessed over TCP.
Milestones / functionality:
Protocol specifications:

1. Request: PUT [<key>] <value>  
    a. Stores the key and value mapping  
    b. Return: “!200”  
2. Request: GET <key>  
     a) Returns the value corresponding to the key given  
           i) Return: “!200 <value>”  
      b) If <key> does not exist, return: “!400”  
3. Request: DEL <key>  
     a) If <key> exists, delete it from your store. Specifically, any subsequent GET query must return   
         “!400” unless the key has been reset.  
      b) Regardless of existence, return “!200” if no other error occurred.  
4. <key> details (not a command/request)  
      a) Can be expected to be ASCII printable characters.  
      b) Static max size (as defined by you, bonus: make it configurable).  
5. <value> details (not a command/request)  
      a) Can be expected to be ASCII printable characters as well.  
      b) Static max size  
