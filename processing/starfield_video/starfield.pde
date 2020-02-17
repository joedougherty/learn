import ddf.minim.*;
import ddf.minim.analysis.*;

Minim minim;
AudioPlayer song;
BeatDetect beat;

Star[] stars = new Star[2500];

void setup() {
  size(1360, 768);
  
  for (int i=0; i<stars.length; i++) {
   stars[i] = new Star(); 
  }
  
  minim = new Minim(this);
  song = minim.loadFile("eeeeeeeeeeee_session.mp3");
  song.play();
 
  beat = new BeatDetect();
}

void drawField(float spd, boolean spike) {
  for (int i=0; i<stars.length; i++) {
   stars[i].update(spd);
   if ((spike == true) && (i % 4 == 0)) {
     int d3 = int(map(random(0,1), 0, 1, 1, 3));
     int c = #30ff4c;
     if (d3 == 1) {
       c = #30ff4c;
     } else if (d3 == 2){
       c = #c2c2d6;
     } else {
       c = #9999ff;      
     }
     stars[i].show(c, map(random(0,1), 0, 1, 1, 2));
   } else {
     stars[i].show(235, 1);
   }
  } 
}

float base_spd = 0;

void draw() {
  background(#0e0112);
  translate(width/2, height/2);
  
  beat.detect(song.mix);
    
  if (beat.isOnset()) {
    drawField(base_spd + .005, true);
    base_spd = base_spd + .001;
  } else {
    drawField(base_spd, false);
  }
}
