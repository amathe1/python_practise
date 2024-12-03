import re

def main():
    text = "You could get a developer job. E.g. in robotics. Maybe. Or web development."

    # Very complex explanation !! Look at below video for clear explanation
    # https://caveofprogramming.teachable.com/courses/python-machine-learning-beginners/lectures/46041139
    results = re.findall(r"\s+(\w+)\.(?=\s+|$)", text)

    print(results)


main()