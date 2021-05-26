# 2021-USMC-Calculator-Website
<h4>5/25/2021</h4>
<p style="margin-left:10%"; margin-right:10%;">As the calculator continues to grow, it becomes tedious to maintain two separate repositories for essentially the same program. The website application continues to use the original Python code and has grown significantly over the past 10 days. With the assistance of the Streamlit module, I’ve been able to deploy my program much faster than anticipated.  
    <li>  Combat Fitness Test (CFT) scoring is now active.</li>
    <li>  The web application can be accessed at the following link. <a href=https://share.streamlit.io/brogers1812/2021-usmc-calculator-website/main/index.py>2021 USMC Calculator</a></li>
<h5>Way Ahead</h5>
    <li> The web app still needs a lot of editing for easier user interface </li>
    <li> I’m having issues with times that end in “.00”. The program coverts the code from 3.00 to 30 which isn’t read in my CSV files. Will need to continue to troubleshoot. </li>
    <li>  Quality assurance by field testing </li>

<h4>5/23/2021</h4>
<p style="margin-left:10%"; margin-right:10%;">So I made a pretty big oversight on the project. In January 2021, the Marine Corps released a new publication covering changes in the PFT. MCO 6100.13A with CH-3 (located in the resources folder) outlines the addition of performing a plank rather than crunches. While I didn't catch it while creating this program, I did capture this change in the website version. I'll make the appropriate changes but my priority has focused on taking this code and creating a web app. You can find the web app repository at <a href="https://github.com/brogers1812/2021-USMC-Calculator-Website">2021-USMC-Calculator-Website</a>.</p> 
    <li>  Found a solution for rounding the run times.</li>
    <li>  Beta version of the website is stabilized on local server.</li>
<h5>Way Ahead</h5>
    <li>  Implement the plank event into the program</li>
    <li>  Review code for redundancy</li>
    <li>  Increase compatibility of user interface</li>
<h4>5/21/2021</h4>
<p>
    <li>  Completed all CSV lookup tables.</li>
    <li>  Added quality assurance folder to record data input/output accuracy (continuous testing)</li>
    <li>  Program is completed.</li>
</p>
<h5>Way Ahead</h5>
<p>
    <li>  Continue researching in accounting for runtime to next highest minute</li>
    <li>  Develop for website implementation</li>
    <li>  Test for bugs</li>
</p>
<h4>5/20/2021</h4>
<p>
    <li>  Completed all CSV tables except 5000 meter row. </li>
    <li>  Push ups and pullup scores account for either one and male or female choice.</li>
    <li>  Quite a few more updates since May 18th.</li>
</p>
<h5>Way Ahead</h5>
<p>
    <li>  Create the 5000 meter row scoresheets</li>
    <li>  Update code to reflect male or female input for scoring crunches</li>
    <li>  Begin research in accounting for runtime to next highest minute</li>
</p>
<h4>5/18/2021</h4>
<p>
    <li> Removed functions to shorten code and remove redundancy.</li>
    <li> Created table to lookup male run times without altitude consideration. </li>
    <li> Inputted user input for run times. Round up to the nearest tenth.</li>
</p>
<h5>Way Ahead</h5>
<p>
    <li> Round times (26:52) to 27:00 and not 26:60. </li>
    <li> Compute a total score for a male performing pullups, crunches, and a run time. </li>
    <li> Consider the code to implement female scores (if/else).</li>
</p>      
<h4>5/17/2021</h4>
<p>
    <li>  Wrote code to receive input for age, gender, high altitude, and pullups.</li>
    <li>  Created table to lookup pullups for males.</li>
    <li>  Program provides output of pullup score for males.</li>
</p>
<h5>Way Ahead</h5>
<p>
    <li>  Test for bugs.</li>
    <li>  Find solution if input is out of bounds on table. </li>
    <li>  Begin coding for male crunches.</li>
</p>

<h4>5/15/2021</h4>
<p>This program will be designed to calculate PFT & CFT scores based on users input. It will be divided into categories such as Male/Female, Age, Altitude, Pullups, Crunches, Planks, and etc...</p>

![image](https://raw.githubusercontent.com/brogers1812/2021-USMC-Calculator/main/information/Slide1.JPG)
![image](https://raw.githubusercontent.com/brogers1812/2021-USMC-Calculator/main/information/Slide2.JPG)

