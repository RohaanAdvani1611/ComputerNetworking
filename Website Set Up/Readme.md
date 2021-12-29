Website Set Up
This assignment requires you to connect your mobile phone to 4G network, create a hot-spot on mobile phone and connect the laptop to this Wi-Fi hotspot.

Part 1

Install apache2 web server on your laptop.

Use the command

$ sudo apt install apache2

Add a folder called /var/www/html/tmp/ and write a file called hello.html there

Access the tmp/hello.html file of the website using browser on laptop and IP address of 127.0.0.1; Take a screenshot, and call it:  laptop1.png

Connect your laptop to the Wi-Fi hotspot created from your mobile phone.

Run "ifconfig" on mobile phone (using terminal) and on laptop and ensure that they are in the same network.

Access the tmp/hello.html file on web server (on laptop), from your mobile phone browser. Take a screenshot, and call it phone1.png The screenshot should clearly show the IP address used for accessing the website and the same content as in laptop1.png

Part 2

Install A web server on your mobile phone. One such App on android is "Simple http-server".  Note: you can use any app.

Start running that server.

Access the web-site running on the mobile phone, from the browser on your laptop. Take a screenshot. Call it laptop2.png

Learn on your own, how to give the web-server, an access to a particular folder on your mobile phone, and create the folder "tmp" and file hello.html on your smartphone, so that it's accessible using browser.  Access using browser on laptop   http://<IP-address-of-smartphone>/tmp/hello.html  and take a screenshot. Name it laptop3.png

Ask anyone around for some help with his/her smartphone. Use his/her smartphone to connect to the wi-fi hotspot network created by your smartphone. Now access the web-site and the file tmp/hello.html running on your mobile phone, from the browser on the mobile phone of your friend. Take a screenshot. Call it phone2.png

Submission

(Note: Line below has a regular expression syntax!)

Submit the 5 files: laptop[123].png and phone[12].png   

compressed into one single MISID.zip file

Additional Tasks:

If you are more enthusiastic, then do the following tasks, for no extra marks: Learn how to setup multiple websites using single apache2 server, learn how to configure apache2 to handle 3000 simultaneous connections, learn how to configure the HTTP server on your mobile phone to server web-pages that you have created.
