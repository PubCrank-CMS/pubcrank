---
template: post
categories:
  - PubCrank
  - Release
draft: false
title: Introducing PubCrank.com
description: 'Official launch of PubCrank.com, static site editor with rails for non-devs.'
date: 2024-03-09T06:00:00.000Z
cover: /img/pubcrank.png
---
Today I'm officially releasing [PubCrank.com](https://www.pubcrank.com/)! PubCrank is CMS for static site generators that use Markdown to generate content. It lets a developer setup a static site with guards that can guide content creators and editors to develop content independently. It does this with a simple editor that is configurable with templates that define the fields which can be used for that particular type of content. See the screenshot of the editor below.

![PubCrank Screenshot](/img/pubcrank-editor.png)

## Why Another CMS?

I've developed various Content Management Systems over the years, most notably, I was a founding engineer of [CultureMap.com](https://culturemap.com/). And for the most part these systems all work the same. They present various form fields which need to be filled in and usually have one big field for free-form content. It is then up to the developer to define these fields and take them to fill in an HTML template which is shown to visitors of your site.

I've also found over the years, that for most smaller organizations unless you have dedicated editors or writers, everyone says they want to help edit content, but usually it is left up to the developer. So instead of setting up a hard to maintain CMS, I have started to use static site generators like [Hugo](https://gohugo.io/) with Markdown. This setup follows the same model as other CMS's with fields defined in the frontmatter and content as Markdown in the main body of the file.

However, every once in a while, I get lucky and someone wants to help develop content. They are essentially locked out of helping without a CMS. Thus, the CMS for static sites was born. I've found a few existing static site CMS tools but was not satisfied with the workflow and experience. So I developed [PubCrank.com](https://www.pubcrank.com/) to fill this gap.

## Free for Local Editing

I wanted to build and deploy PubCrank as fast as possible with the most bare bones feature set so that I could start using it with several small sites that I maintain. Additionally, I would like to make some revenue selling it as a SaaS. By using the [Native File System API](https://developer.chrome.com/docs/capabilities/web-apis/file-system-access) I was able to build the PubCrank Editor with only frontend technology and without the need for building something like an Electron app. So today's launch is that initial release.

You can edit sites with PubCrank locally right in your browser. This will let you setup guards for your writers but still means they will probably need to use something like Git when they are done developing content. However, this is a great way for you to start setting up and using PubCrank as a developer.

I've decided to keep this local editing free forever as an on ramp for using PubCrank. If you're a developer and only ever need a nice editor experience than today's release is all you'll ever need.

## Future in the Cloud

If, however, you would like an even easier experience for your writers, I plan to add future integrations with Github, Gitlab, etc. This will allow you to provide an editing experience without the need for Git locally. PubCrank will handle all the commits and pushes for your users.

This is where I plan to charge for the PubCrank service since this will mean maintaining backend services unlike today's launch which is simply a frontend static file deployment.

So try PubCrank today, to start cranking out your content! In case you missed the screenshot, this post was written with PubCrank.

<iframe src="https://giphy.com/embed/v2xIous7mnEYg" width="300" height="218" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/newspaper-press-v2xIous7mnEYg">via GIPHY</a></p>

## PubCrank Links

- Try PubCrank today: [https://www.pubcrank.com/](https://www.pubcrank.com/)
- [Discuss Features and Ideas](https://github.com/pizzapanther/pubcrank-community/discussions)
- [Report Issues](https://github.com/pizzapanther/pubcrank-community/issues)

