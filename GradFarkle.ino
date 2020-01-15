//Grad Farkle
//Tommy Shu
//May 29, 2019

//Description:
//Turns the Adafruit Circuit Playground into a grad decoration.
//Neopixels flash varying intensities of red and blue
//When the right button is pressed a popular grad tune plays

#include <Adafruit_CircuitPlayground.h> //import circuit playground library

#define a1 220
#define b1 247
#define c  262
#define cs 277
#define d  294
#define e  330
#define f  349
#define fs 370
#define g  392
#define a  440
#define bf 446
#define b  494
#define C  523
#define D  587
#define E  659


void setup() {
  // put your setup code here, to run once:
  randomSeed(analogRead(0));
  CircuitPlayground.begin();

}

void centaur_lights() {
  //Sets every second neopixel to a random red brightness
  //Sers every second neopixel to a random blue brightness

  //loop counter for every 2 neopixels
  int colorit_i = 0;
  //which neopixel (0-9?) is being set
  int pixelnum = 0;
  //random level of r where 0-200 is possible
  int rand_brightness_red = random(200);
  //random level of r where 0-200 is possible
  int rand_brightness_blue = random(200);

  //1000 = 1 second
  delay(100);

  if (pixelnum == 11) {
    pixelnum = 0;
  }
  else {
    for (colorit_i = 0; colorit_i <= 6; colorit_i++) {
      CircuitPlayground.setPixelColor(pixelnum++, rand_brightness_red, 0, 0);
      CircuitPlayground.setPixelColor(pixelnum++, 0, 0 , rand_brightness_blue);
    }
  }
}

void play_grad_farkle_tune() {
  //plays a grad_farkle tune when the right button is pressed:

  //notes in the melody
  int melody[] = {
    g,f,g,a,e,d,c,b1,c,d,a1,a1,b1,cs,d,e,a
  };

  //note duration: 4 = quarter note, 8 = eight note
  int noteDurations[] = {
    1,4,4,2,1,1,1,4,4,2,1,1,1,4,2,4,1
  };

  if (CircuitPlayground.rightButton())
  {   // play when we press the right button
    for (int thisNote = 0; thisNote < 18; thisNote++) { //play notes of the melody
      // to calculate the note duration, take one second divided by the note type.
      // e.g. quarter note =1000/4, eighth note = 1000/8, etc.
      int noteDuration = 1000 / noteDurations[thisNote];
      CircuitPlayground.playTone(melody[thisNote], noteDuration);

      // to distinguish the notes, set a minimum time between them.
      //   the note's duration +30% seems to work well:
      int pauseBetweenNotes = noteDuration * .8;
      delay(pauseBetweenNotes);
    }
  }
}


void loop() {
  // put your main code here, to run repeatedly:
  centaur_lights();
  play_grad_farkle_tune();
}
