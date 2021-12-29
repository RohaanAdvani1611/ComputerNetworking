TCP Chatroom
Write a TCP client-server  (in Python, C or Java) application that implements a chat server, using multi-threading. Both client and server can be multi-threaded.

You should submit two files:  server.py and client.py  (the extension can change depending on the language) compressed into a single file MISID.tar.gz

The programs should run like this:

$ python server.py <port-no> # and now server is running 

$ python client.py <port-no> <username>

Where <username> will be shown as your name for chatting.

While <port-no> is the port number to which the server binds itself.

You can be ignorant towards "proper" closure of all threads and client/server when one of them terminates, and your evaluator will be ok if you terminate them in the crude fashion of pressing ctrl-c.

Each client will send messages to the server and the server will ensure that everyone sees messages from everyone else. (So this will be more like a broadcast chatroom). You are not expected to support a 1-1 communication, but only a broadcast by everyone.

Example of output (with 3 clients, having announced their names as Amol, Ashish, Nitesh). Note that the name is to be announced by client only on command line once, it is not part of every message that you send, but still it should be seen with every message shown to everyone.  This is the output that everyone sees. 

Amol: Hi
Ashish: Hello everyone
Amol: Hi Ashish
Nitesh: Vanakkam
Amol: Hey Nitesh
Ashish: Done assignment?
Amol: Hi!
Nitesh: Not done yet
Ashish: I'm done !
