import datetime

now = datetime.datetime.now()

def get_season(month):
    if month in [12, 1, 2]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    else:
        return 'fall'

season = get_season(now.month)

image_addr = {
    'winter': 'img/winter.jpg',
    'spring': 'img/spring.jpg',
    'summer': 'img/summer.jpg',
    'fall': 'img/fall.jpg'
}

selected_image_path = image_addr[season]

with open('readme.md', 'r') as file:
    readme_content = file.read()

readme_content = readme_content.replace('![Seasonal Image](img/season.jpg)', f'![Seasonal Image]({selected_image_path})')

with open('readme.md', 'w') as file:
    file.write(readme_content)
