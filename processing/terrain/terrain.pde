import ddf.minim.*;
import ddf.minim.analysis.*;

Minim minim;
AudioPlayer song;
BeatDetect beat;

int cols, rows;
int scl = 20;
int win_width = 2000;
int win_height = 1200;

float [][] terrain;

float flying = 0;

void setup() {
  frameRate(60);
  
  size(1080, 720 , P3D);
  
  cols = win_width/scl;
  rows = win_height/scl;
  
  terrain = new float[cols][rows];

  float yoff = 0;
  for (int y=0; y<rows; y++) {
    float xoff = 0;
    for (int x=0; x<cols; x++) {
      terrain[x][y] = map(noise(xoff,yoff), 0, 1, -100, 100);
      xoff += 0.2;
    }
  yoff += 0.1;
  }

  minim = new Minim(this);
  song = minim.loadFile("atomicity.mp3");
  song.play();
  
  beat = new BeatDetect();
}

void draw() { 
  flying -= 0.021;
  
  float yoff = flying;
  for (int y=0; y<rows; y++) {
    float xoff = 0;
    for (int x=0; x<cols; x++) {
      terrain[x][y] = map(noise(xoff,yoff), 0, 1, -100, 100);
      xoff += 0.125;
    }
  yoff += 0.1;
  }  
  
  background(0);
  strokeWeight(.8);
  stroke(#9900cc);
  noFill();
  
  translate(width/2, height/2);
  rotateX(PI/3.1);
  
  translate(-win_width/2, -win_height/2);
 
  for (int y=0; y<rows-1; y++) {
    beginShape(TRIANGLE_STRIP);
    for (int x=0; x<cols; x++) {
        vertex(x*scl, y*scl, terrain[x][y]);
        vertex(x*scl, (y+1)*scl, terrain[x][y+1]);
    }
    endShape();  
  }
}
