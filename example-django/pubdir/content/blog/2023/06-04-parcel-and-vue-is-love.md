{
  title: Using Vue 3 with Parcel JS
  date: 2023-06-03 00:00:00-0600
  categories:
  [
    vue
    parcel
    javascript
    development
  ]
  cover: /img/parcel-vue.jpg
  canonical_url: https://hackernoon.com/using-vue-3-with-parcel-js
  template: post.html
}


While all the buzz lately is around the Javascript build tool [Vite](https://vitejs.dev/) especially in the Vue.js community, I still prefer [Parcel](https://parceljs.org/) for building my Vue.js applications. However, getting started with Vue.js and Parcel is a little tricky because most tutorials and docs focus around Vite or other more popular build tools. This article documents how to setup Parcel to build a Vue.js project. But first why would even want to use Parcel?

## Why Use Parcel?

While Vite works great and builds applications fast, it's focus is on building things fast. That sounds great to a lot of people probably, for me that is an anti-pattern. Yes I want my devs tools to be fast, but if that is the primary focus, then often times the developer experience is often a secondary concern. Instead, I want developers tools that are primarily focused on developer experience and also fast. I think that Parcel delivers great on this promise. Most Javascript build tools like Vite end up being wrappers around existing tools but with the configuration obscured away and pre-configured for you. While this is great to get started fast, you eventually hit configuration roadblocks and complexity as your app grows. Parcel has a zero-configuration philosophy and is not a wrapper around older tools. Once you get past setting it up, you encounter far fewer configuration roadblocks as your app grows.

The only downside with using Parcel especially with Vue, is that the setup is not documented as much as I would like. Additionally, with the release of Parcel 2 and Vue 3 there are a few quirks with the setup. Hopefully, they will get worked out in the future, but for now, the instructions below will show you how to setup a Vue app with Parcel.

## Building a Vue 3 App with Parcel

To get started, first you need a Vue 3 app. If you need to start one, the [Parcel documentation](https://parceljs.org/languages/vue/) is a good place to get a skeleton app to start with. If you use just those instructions though, you'll probably get some errors or warnings we need to take of.

### Fix 1: package.json - Vue Bundle

In your `package.json` you'll want to add an alias section. This will let Parcel know the correct version of Vue to use when bundling your application.

```json
"alias": {
  "vue": "vue/dist/vue.esm-browser.js"
},
```

#### Special Note for Production Builds

Right now there is [a bug](https://github.com/parcel-bundler/parcel/issues/7663) when you switch to production builds with Vue 3 and Parcel. So when you do a production build you need to switch the alias to `vue.esm-browser.prod.js`. I just use a pre-build command in my CI/CD to switch that out for production builds: `sed -i 's/vue.esm-browser.js/vue.esm-browser.prod.js/g' package.json`

### Fix 2: package.json - Build type (may be needed)

Depending on your build target and your output context you may want to add `type` and `targets` also to your `package.json`. It doesn't hurt to add them and to be explicit about what you're building. I also like to use `targets` often because I want Parcel to build multiple things.

```json
"type": "module",
"targets": {
  "myapp": {
    "source": "src/index.js",
    "distDir": "dist",
    "context": "browser",
    "outputFormat": "global"
  }
},
```

### Fix 3: Main App JS - Silence More Warnings and Include Vue Options API

In your you main app JS, you are probably getting additional warnings or you may want to include the Vue Options API. Put these variables in you initial app JS file to silence the dev tool warnings and explicitly setup the Vue Options API or not. You probably want to put them towards the top of the file.

```javascript
__VUE_OPTIONS_API__ = true;

if (process.env.NODE_ENV !== 'production') {
  __VUE_PROD_DEVTOOLS__ = true;
} else {
  __VUE_PROD_DEVTOOLS__ = false;
}
```

Have fun with your new Vue 3 app development and throw out your aspirin as you'll now be on easy street and have far fewer configuration errors. Parcel JS will handle most other setup, even installing the transformers you'll need to compile things like Vue Single File Components and Typescript.

## Update 2024

Just use Vite because Parcel JS almost always fails for me now. Unfortunately, it's no longer a viable option.

Check out [this article](https://wildermuth.com/2021/01/10/Vite-for-Existing-Vue-CLI-Projects/) for a quick Vite setup.
