{
  title: Setting the Default Sound Source and Sink on Ubuntu
  date: 2023-09-06 00:00:00 -0600
  categories:
  [
    audio
    pulse audio
    bash
    pactl
  ]
  cover: /img/pulseaudio.png
}


If you're a modern office worker you probably do a lot of video calls and it's really annoying when your default audio and video inputs and outputs change on rebooting your computer. Windows is actually pretty good at remembering your last choice and setting the appropriate defaults on reboot. However, Linux doesn't do anything here, so you're at the mercy of randomness unless you have a script to set the default for you. Below is a script you can add to your startup applications which will set your default audio input and output for systems that use [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio/) like Ubuntu and Debian. It should work on other systems with PulseAudio as well.

To use the script, modify lines 9-10 and lines 15-16 with your default audio source and sink. To find out what they might be named, use `pactl list short sinks` and `pactl list short sources`. Then craft a search string for the grep statement to check if they are available and also enter the full name for lines 15 and 16.

{{< prismjs lang="bash" line-numbers="true" >}}
#!/usr/bin/env bash

sleep 5

pactl=$(which pactl)
if [[ -x "$pactl" ]]
then
  # Modify lines below for SOURCE and SINK check
  SINK=`pactl list short sinks | grep SINK-STRING -c`
  SOURCE=`pactl list short sources | grep SOURCE-STRING -c`
  if [[ $SOURCE = 1 ]] && [[ $SINK = 1 ]]
  then
    echo "Setting Audio Source and Sink"
    # Modify lines below for full SOURCE and SINK name
    pactl set-default-source FULL-SOURCE-STRING
    pactl set-default-sink FULL-SINK-STRING
  fi
fi
{{< /prismjs >}}
