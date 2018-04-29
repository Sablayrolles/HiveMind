using Android.App;
using Android.Widget;
using Android.OS;
using Android.Media;
using System.Timers;
using Android;
using System;

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
            Button buttonRec = FindViewById<Button>(Resource.Id.buttonRec1);
            // Get the button "Stop"
            Button buttonStop = FindViewById<Button>(Resource.Id.buttonStop1);
            // Get the Seek Bar
            SeekBar seek = FindViewById<SeekBar>(Resource.Id.seekBar1);
            // Get the TextView where we display the Seek Bar information
            TextView displaySec = FindViewById<TextView>(Resource.Id.textView1);
            // Get the text field to enter the file name
            EditText fileName = FindViewById<EditText>(Resource.Id.editText1);
            // Get the chronometer
            Chronometer chrono = FindViewById<Chronometer>(Resource.Id.chronometer1);
            // Create a media recorder
            MediaRecorder recorder = new MediaRecorder();
            // Create the path where the audio file will be written
            string storage_path = Android.OS.Environment.ExternalStorageDirectory.AbsolutePath;
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
                // Set the variable to increment file name to 1
                i = 0;
                // Disable editText
                fileName.Enabled = false;
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
                // Enable the file name text edit
                fileName.Enabled = true;
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
                string f_path;
                f_path = storage_path + "/music/" + fileName.Text + nb + ".3gpp";

                recorder.SetAudioSource(AudioSource.Mic);
                recorder.SetOutputFormat(OutputFormat.ThreeGpp);
                recorder.SetAudioEncoder(AudioEncoder.Aac);
                recorder.SetOutputFile(f_path);
                recorder.Prepare();
                recorder.Start();
            }

            // Stop audio record
            void stopAudioRecord()
            {
                recorder.Stop();
                recorder.Reset();
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

