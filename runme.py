def main():
    title = input('博客标题：')
    subtitle = input('子标题：')
    description = input('描述：')
    keywords = input('关键字：')
    author = input('作者：')
    username = input('Github用户名：')
    email = input('Email：')
    date = input('建站时间（年, 月, 日）：')

    with open('./_config.yml.src', 'r', encoding='utf-8') as src:
        text = src.read().format(title=title, subtitle=subtitle,
                                 description=description, keywords=keywords,
                                 author=author, username=username)
        with open('./_config.yml', 'w', encoding='utf-8') as dst:
            dst.write(text)

    with open('./themes/matery/_config.yml.src', 'r', encoding='utf-8') as src:
        text = src.read().format(username=username, email=email)
        with open('./themes/matery/_config.yml', 'w', encoding='utf-8') as dst:
            dst.write(text)

    with open('./themes/matery/layout/_partial/footer.ejs.src',
              'r', encoding='utf-8') as src:
        text = src.read().format(author=author, date=date)
        with open('./themes/matery/layout/_partial/footer.ejs',
                  'w', encoding='utf-8') as dst:
            dst.write(text)


if __name__ == '__main__':
    main()
    print('done')
