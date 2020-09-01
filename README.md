# urlencoder
urlencoder is a tool written in python 3. It can be used for hex encoding or decoding a URL.<br>
<b>For an example:</b>
  <pre>http://www.google.com?search=hello+world</pre>
<b>can be written in hex encoding as:</b>
  <pre>http%3A%2F%2Fwww.google.com%3Fsearch%3D%22hello%2Bworld%22</pre>
<b>or</b>
  <pre>%68%74%74%70%3a%2f%2f%77%77%77%2e%67%6f%6f%67%6c%65%2e%63%6f%6d%3f%73%65%61%72%63%68%3d%68%65%6c%6c%6f%2b%77%6f%72%6c%64</pre>
  
So, we saw that the URL can be encoded either partially or fully. The <b>urlencoder</b> supports both type of encoding. It can perform both encoding and decoding function.


# Reason to use
As everybody knows that <b>XSS(Cross Site Scripting)</b> is the most common vulnerability on the internet, people are likely to receive a malicious URL which can't be identified easily if it's partially or fully hex encoded. In such cases, we can use <b>urlencoder</b> to decode the hex encoded string and see the real UTF-8/ASCII string behind it.

The <b>urlencoder</b> comes with an XSS detector which detects if there is any <script> tag present in the URL. So it can perform XSS attack payload detection. If the URL in unsafe, it will present with a warning.
  
# Why I built it?
I personally built it to save my time while testing machines/boxes for XSS vulnerability. Without an application like <b>urlencoder</b>, I have to visit websites like <a href="https://www.url-encode-decode.com/">url-encode-decode</a> to do the same task. I was sick of doing that. Also, I found out that these websites just perform partial URL hex encoding. What if an attacker presents a URL which is fully hex encoded? So, I decided to build this tool up so that I can fire fully hex encoded attack payloads and also can check URLs for it's presence.

# How to use?
<ul>
  <li>First of all, clone the project in your desired directory by using the following command:<br>
    <pre><i>git clone https://github.com/xscorp/urlencoder.git</i></pre><br>
  <li>Run the application using python interpreter:<br>
    <b>Linux</b>:<br>
    <pre><i>./urlencoder</i></pre><br>
    <b>Windows</b>:<br>
    <pre><i>urlencoder</i></pre><br>
  <li>After issueing the following commands, you will be presented with a message that you need to supply mandatory arguments. Type <b>--help</b> to see options/help menu to understand features and usage of the program like this:
    <pre><i>./urlencoder --help</i></pre>
</ul>

 # NOTES:
 <ul>
  <li>If your code isn't working, check if you are running the program with python 3 interpreter and not python 2 interpreter.
  <li>If you are still getting error, then check if you have passed the mandatory parameter <b>--url</b>. Yea I know it's weird that you need to use --url for everything in urlencoder but it increases readablity of the code. <b>If you don't have any URL to paas for --url flag, just pass any random test string or empty quotes("")</b>
  <li>Why it doesn't support Advance XSS scanning? Well, Right now, I am not armed with enough knowledge so I can't build that for now. But I will surely work on this project later on.
  <li>If you find any bugs in it, feel free to contact me or comment here. 


## Created by:
Shashank Barthwal     
Harshika Negi(harshika21111999@gmail.com)
