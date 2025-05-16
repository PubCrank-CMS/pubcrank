{
  title: Android Privacy Protocol
  date: 2021-07-06 20:00:00 -0600
  categories: [
    android,
    privacy,
  ]
  canonical_url: https://hackernoon.com/have-your-privacy-cake-on-android-and-eat-it-too-db1f37b5
  cover: /img/android.jpg
  template: post.html
}

Recently I've had the goal to reduce my usage of big tech products and thus reduce the tracking and influence they have in my life. One of the biggest areas to reduce is the phone. Modern Android has all kinds of hooks so that apps and Google services can track you. And it is almost impossible for you to turn off these services and still have the ability to use everyday applications.

My first attempt to reduce tracking was to try operating systems such as [CalyxOS](https://calyxos.org/) and [GrapheneOS](https://grapheneos.org/). These operating systems do a great job of removing Google services, but the trade-off is that you can use fewer applications because many depend on these services.

[CalyxOS](https://calyxos.org/) comes built-in with [MicroG](https://microg.org/) which attempts to fill in for these services, however, there are still some apps that do not function well with a Google substitute. Through the usage of these OS's though, I have been able to come up with a privacy protocol to use with a normal Android phone to increase privacy while still maintaining application compatibility.

## Android Privacy Protocol

The Android Privacy Protocol is a set of methods to configure and use your Android phone to increase your privacy with any standard Android phone while also having the ability to use most modern apps.

A general overview of the protocol:

- Keep the default profile anonymous (don't log into a Google account)
- Use the [Aurora Store](https://auroraoss.com/) to install applications
- Use a "Work" profile for any Google or other apps you wish to contain and restrict usage

## How the Protocol Works

Android has long given you the ability to not log into your Google account and thus function anonymously;
however, when you do this, you lose the ability to install applications from the Play Store. You will still receive updates of existing installed apps. To get around this, we use the third-party Play Store app, the [Aurora Store](https://auroraoss.com/). This allows you to download apps from the Play Store without using the Play Store. And thus, you can now use most apps without logging in with a Google account.

The last part of the protocol is to use a "work" profile for applications that you need a Google account for. Android allows you to have multiple users/profiles, however, by default you have to log out of one profile and switch to another. This is useful but can be cumbersome if you use it daily. We can do better! Android also includes a feature that allows you to use a "work" profile side by side with your personal apps. However, this feature is not accessible and usually only available to enterprise devices. What is interesting though is this feature is available to modern Android users if you have an app that will turn it on for you. The [Shelter app](https://play.google.com/store/apps/details?id=net.typeblog.shelter&hl=en_US&gl=US) lets you access this feature even though it might be hidden. In addition to application isolation, the Shelter app lets you shut down all your "work apps" at once. So you can use your favorite apps, shut them down quickly and isolate their data access to curtail some of their trackings.

## The Setup

Let's go over the details of how to set up your phone with the Android Privacy Protocol.

1. Starting with a new phone, go through the Android setup but make sure to skip Google account setup and restoring from another account or phone. You can still use things like fingerprint unlock but make sure not to connect a Google account.
2. Let the Play Store apply the latest updates.
3. Install the [Aurora Store](https://auroraoss.com/). You can feel free to log into Google here if you wish to have access to your paid apps. The Aurora Store does not connect the Google account outside the app.
4. Install the [Shelter app](https://play.google.com/store/apps/details?id=net.typeblog.shelter&hl=en_US&gl=US) from the [Aurora Store](https://auroraoss.com/) and setup your "work profile". This is where you can log into your Google account if you wish to keep it isolated. Note: if you have trouble installing Aurora or the Shelter App it might be easier to install [F-Droid](https://f-droid.org/) first, then install those apps from there.
5. Continued usage: Install personal apps from the Aurora Store and work apps from the Play Store (under your work profile).

Note: If you have trouble finding applications on the [Aurora Store](https://auroraoss.com/) then use the Play Store under your work profile. Using the Shelter app, you can then clone the app to your personal profile. Lastly, if you wish, you can remove the app from your work profile.

## Final Words

I still have to do some research on how private using Android mostly anonymously is, but in theory, I think it is a huge gain. I think this method is a good way to stay private while also having access to the widest variety of apps.

