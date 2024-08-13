from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(req):
    return HttpResponse("<center><img src='https://media.tenor.com/hm6dEqOq7q8AAAAM/endhiran-chitti.gif' width='50%'/></center>")


def about(req):
    return HttpResponse('''<div style="background-color: #f4f4f4; padding: 50px 20px; text-align: center;">
    <div style="color: #2c3e50; font-size: 3em; font-weight: bold;">About Us</div>
    <div style="color: #7f8c8d; font-size: 1.2em; margin-top: 10px;">We create exceptional digital experiences</div>
</div>

<div style="padding: 20px; max-width: 1200px; margin: 0 auto;">
    <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 20px;">Our Mission</div>
    <div style="font-size: 1em; color: #555; margin-bottom: 40px;">
        Our mission is to deliver high-quality digital solutions that transform businesses and enrich user experiences. We believe in innovation, creativity, and the power of technology to drive positive change.
    </div>

    <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 20px;">Our Vision</div>
    <div style="font-size: 1em; color: #555; margin-bottom: 40px;">
        We envision a world where technology seamlessly integrates into everyday life, enhancing the way people interact, work, and live. We strive to be at the forefront of this transformation, guiding businesses through the digital landscape with expertise and passion.
    </div>

    <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 20px;">Our Values</div>
    <div style="font-size: 1em; color: #555;">
        <ul style="list-style-type: none; padding: 0;">
            <li style="margin-bottom: 10px;">Innovation: We constantly seek new ways to solve problems.</li>
            <li style="margin-bottom: 10px;">Integrity: We operate with transparency and honesty.</li>
            <li style="margin-bottom: 10px;">Customer-Centric: We put our clients' needs first.</li>
            <li style="margin-bottom: 10px;">Excellence: We strive for the highest quality in all we do.</li>
        </ul>
    </div>
</div>
''')

def contact(req):
    return HttpResponse('''<div style="background-color: #f4f4f4; padding: 50px 20px; text-align: center;">
    <div style="color: #2c3e50; font-size: 3em; font-weight: bold;">Contact Us</div>
    <div style="color: #7f8c8d; font-size: 1.2em; margin-top: 10px;">We'd love to hear from you! Fill out the form below to get in touch.</div>
</div>

<div style="padding: 20px; max-width: 1200px; margin: 40px auto; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between;">
    <div style="flex: 1; min-width: 300px; margin-right: 20px;">
        <img src="https://www.searchenginejournal.com/wp-content/uploads/2022/08/contact-us-2-62fa2cc2edbaf-sej.png" alt="Contact Us" style="width: 100%; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
    </div>
    <div style="flex: 1; min-width: 300px;">
        <form action="#" method="post" style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <div style="margin-bottom: 20px;">
                <label for="name" style="font-size: 1.2em; color: #2c3e50;">Name:</label>
                <input type="text" id="name" name="name" style="width: 100%; padding: 10px; margin-top: 5px; font-size: 1em; border: 1px solid #ccc; border-radius: 5px;" required>
            </div>

            <div style="margin-bottom: 20px;">
                <label for="email" style="font-size: 1.2em; color: #2c3e50;">Email:</label>
                <input type="email" id="email" name="email" style="width: 100%; padding: 10px; margin-top: 5px; font-size: 1em; border: 1px solid #ccc; border-radius: 5px;" required>
            </div>

            <div style="margin-bottom: 20px;">
                <label for="subject" style="font-size: 1.2em; color: #2c3e50;">Subject:</label>
                <input type="text" id="subject" name="subject" style="width: 100%; padding: 10px; margin-top: 5px; font-size: 1em; border: 1px solid #ccc; border-radius: 5px;" required>
            </div>

            <div style="margin-bottom: 20px;">
                <label for="message" style="font-size: 1.2em; color: #2c3e50;">Message:</label>
                <textarea id="message" name="message" rows="5" style="width: 100%; padding: 10px; margin-top: 5px; font-size: 1em; border: 1px solid #ccc; border-radius: 5px;" required></textarea>
            </div>

            <div style="text-align: center;">
                <button type="submit" style="background-color: #2c3e50; color: #fff; padding: 10px 20px; font-size: 1em; border: none; border-radius: 5px; cursor: pointer;">
                    Send Message
                </button>
            </div>
        </form>
    </div>
</div>
 ''')

def jobs(req):
    return HttpResponse(''' <div style="background-color: #f4f4f4; padding: 50px 20px; text-align: center;">
    <div style="color: #2c3e50; font-size: 3em; font-weight: bold;">Job Listings</div>
    <div style="color: #7f8c8d; font-size: 1.2em; margin-top: 10px;">Find your next career opportunity</div>
</div>

<div style="padding: 20px; max-width: 1200px; margin: 40px auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px;">
    <!-- Job 1 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">Software Engineer</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $80,000 - $100,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job1')">View Job Description</div>
        <div id="job1" style="display: none; margin-top: 10px; color: #555;">
            <p>Develop, test, and maintain software applications...</p>
        </div>
    </div>

    <!-- Job 2 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">Product Manager</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $90,000 - $120,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job2')">View Job Description</div>
        <div id="job2" style="display: none; margin-top: 10px; color: #555;">
            <p>Lead the product lifecycle from concept to launch...</p>
        </div>
    </div>

    <!-- Job 3 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">Marketing Specialist</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $60,000 - $80,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job3')">View Job Description</div>
        <div id="job3" style="display: none; margin-top: 10px; color: #555;">
            <p>Develop and execute marketing campaigns...</p>
        </div>
    </div>

    <!-- Job 4 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">UI/UX Designer</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $70,000 - $90,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job4')">View Job Description</div>
        <div id="job4" style="display: none; margin-top: 10px; color: #555;">
            <p>Design intuitive and visually appealing user interfaces...</p>
        </div>
    </div>

    <!-- Job 5 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">Data Analyst</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $65,000 - $85,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job5')">View Job Description</div>
        <div id="job5" style="display: none; margin-top: 10px; color: #555;">
            <p>Analyze and interpret complex data sets...</p>
        </div>
    </div>

    <!-- Job 6 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">HR Manager</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $75,000 - $95,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job6')">View Job Description</div>
        <div id="job6" style="display: none; margin-top: 10px; color: #555;">
            <p>Oversee the HR department and manage recruitment...</p>
        </div>
    </div>

    <!-- Job 7 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">DevOps Engineer</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $85,000 - $110,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job7')">View Job Description</div>
        <div id="job7" style="display: none; margin-top: 10px; color: #555;">
            <p>Implement CI/CD pipelines and manage cloud infrastructure...</p>
        </div>
    </div>

    <!-- Job 8 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">Sales Manager</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $70,000 - $90,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job8')">View Job Description</div>
        <div id="job8" style="display: none; margin-top: 10px; color: #555;">
            <p>Lead the sales team to achieve targets and grow revenue...</p>
        </div>
    </div>

    <!-- Job 9 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">Content Writer</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $50,000 - $70,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job9')">View Job Description</div>
        <div id="job9" style="display: none; margin-top: 10px; color: #555;">
            <p>Create engaging content for websites and marketing materials...</p>
        </div>
    </div>

    <!-- Job 10 -->
    <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 1.5em; color: #2c3e50; margin-bottom: 10px;">QA Tester</div>
        <div style="color: #555; font-size: 1.1em;">Salary: $60,000 - $80,000</div>
        <div style="color: #7f8c8d; font-size: 1em; margin-top: 10px; cursor: pointer;" onclick="toggleJobDescription('job10')">View Job Description</div>
        <div id="job10" style="display: none; margin-top: 10px; color: #555;">
            <p>Test software to ensure quality and functionality...</p>
        </div>
    </div>
</div>

<script>
    function toggleJobDescription(id) {
        const jobDescription = document.getElementById(id);
        jobDescription.style.display = jobDescription.style.display === 'none' ? 'block' : 'none';
    }
</script>
 ''')