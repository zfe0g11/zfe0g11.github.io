---
title: Post Blogs With Hexo
top: false
cover: false
toc: true
mathjax: true
date: 2020-11-22 13:50:54
password:
summary: 使用Hexo发布博客
tags:
- 教程
- 博客
categories:
- 博客维护
---

<div align="middle"><iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=858520&auto=1&height=66"></iframe></div>

## 参考

[超详细Hexo+Github博客搭建小白教程](https://zhuanlan.zhihu.com/p/35668237)

## 快速搭建

```bash
# clone我的分支
git clone https://github.com/alexander7xu/alexander7xu.github.io -b raw ./hexo
cd hexo

# 运行python脚本，填写信息
python ./runme.py

# 启动本地服务器，在`localhost:4000`预览效果
hexo clean && hexo g && hexo s

# 一切正常，修改对应位置为你的github用户名，再push到你的GitHub
rm ./_config.yml.src ./themes/matery/_config.yml.src ./themes/matery/layout/_partial/footer.ejs.src
git add *
git commit -m "From alexander7xu"
git branch -D raw
git branch -m hexo
git remote remove origin
git remote add origin https://github.com/你的github用户名
git push origin hexo:hexo
```

## 写文章

```bash
cd $blog_root
hexo new post "post title"
ls source\_posts
```

生成了`post-title`文件夹存放资源文件；`post-title.md`文件存放文章。

## 发布文章

```bash
cd $blog_root
hexo clean && hexo g && hexo s
```
在`localhost:4000`预览效果


```bash
hexo d
```

上传到GitHub

## 备份博客

```bash
cd $blog_root
git add .
git commit -m "message here"
git push origin hexo
```
