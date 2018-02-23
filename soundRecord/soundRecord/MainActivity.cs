using Android.App;
using Android.Widget;
using Android.OS;
using Android.Media;
using System;
using System.Timers;

namespace soundRecord
{
    [Activity(Label = "soundRecord", MainLauncher = true, Icon = "@mipmap/icon")]
    public class MainActivity : Activity
    {
        // Create a timer
        Timer timer;

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            // Set our view from the "main" layout resource
            SetContentView(Resource.Layout.Main);
            // Get the button "Record"
            Button buttonRec = FindViewById<Button>(Resource.Id.buttonRec);
            // Get the button "Stop"
            Button buttonStop = FindViewById<Button>(Resource.Id.buttonStop);
            // Get the Seek Bar
            SeekBar seek = FindViewById<SeekBar>(Resource.Id.seekBar1);
            // Get the TextView where we display the Seek Bar information
            TextView displaySec = FindViewById<TextView>(Resource.Id.textView1);
            // Get the chronometer
            Chronometer chrono = FindViewById<Chronometer>(Resource.Id.chronometer1);
            // Create a media recorder
            MediaRecorder recorder = new MediaRecorder();
            // Create the path where the audio file will be writtent
            string path = "/sdcard/sound";
            // Incremental variable for each sound files
            int i;

            // Display seconds when the value of the seekbar change
            seek.ProgressChanged += (object sender, SeekBar.ProgressChangedEventArgs e) => {
                if (e.FromUser)
                {
                    displaySec.Text = string.Format("{0} seconds", e.Progress+1);
                }
            };

            // Function on click button start
            buttonRec.Click += delegate {
                // Create new timer
                timer = new Timer();
                // Set the variable to increment file name to 0
                i = 0;
                // Disable seekbar
                seek.Enabled = false;
                // Set the timer
                timer.Interval = (seek.Progress + 1) * 1000;
                timer.Elapsed += timerElapsed;
                timer.Start();
                // Chronometer
                chronoStartProp();
                // Audio record
                startAudioRecord(i);
            };

            // Function on click button stop
            buttonStop.Click += delegate {
                // Enable seekbar
                seek.Enabled = true;
                // Kill the timer
                timer.Dispose();
                timer = null;
                // Chronometer
                chronoStopProp();
                // Audio record
                stopAudioRecord();
            };

            // Start chronometer and change its properties
            void chronoStartProp()
            {
                // Show the chrono
                chrono.Visibility = Android.Views.ViewStates.Visible;
                // Disable button rec
                buttonRec.Enabled = false;
                // Enable button stop
                buttonStop.Enabled = true;
                // Start the chronometer
                chrono.Base = SystemClock.ElapsedRealtime();
                chrono.Start();
            }

            // Stop chronometer and change its properties
            void chronoStopProp()
            {
                chrono.Stop();
                chrono.Visibility = Android.Views.ViewStates.Invisible;
                buttonStop.Enabled = false;
                buttonRec.Enabled = true;
            }

            // Start audio record
            void startAudioRecord(int nb)
            {
                string path2;
                path2 = path + nb + ".3gpp";
                // Test : displaySec.Text = path2;
                /*recorder.SetAudioSource(AudioSource.Mic);
                recorder.SetOutputFormat(OutputFormat.ThreeGpp);
                recorder.SetAudioEncoder(AudioEncoder.AmrNb);
                recorder.SetOutputFile(path);
                recorder.Prepare();
                recorder.Start();*/
            }

            // Stop audio record
            void stopAudioRecord()
            {
                /*recorder.Stop();
                recorder.Reset();*/
            }

            // Function which is running each x seconds, where x is the number chosen by the user
            void timerElapsed(object sender, ElapsedEventArgs e)
            {
                stopAudioRecord();
                i++;
                startAudioRecord(i);
            }
        }
    }
}

