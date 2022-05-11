const Engine = Matter.Engine;
const World= Matter.World;
const Bodies = Matter.Bodies;

var engine, world;
var buddy;
var buddyIMG,BoxIMG;
var ground,wall1,wall2,wall3;
var GunI,GunI2,GunI3,Gun,GunG,Gs1,Bs,BSImg;
var ak472,ak47I2,ak47G2;
var Egun,EG,EgG;
var MP,MpI;
var chooseState=0;
var BImg,Board;
var GT,GTI;
var St,StI;
var BGI;
var Gs2;
var live,Lives=100,liveI,L2;
var skill,Skills=100,skillI;
var Pimg,Pistol,PistolG;
var EsI,Es;
var Ps;
var cart,cartI;
var Bomb,BombImg,BombImg2,BombG;
var buddy2;
var Bsound;
var stickbomb,stickbombImg,stickbombG;

var slap,slapI,slapS;
var slaps;
 
var Gskill,GskillI;
var L3;
var heart2,heart2I;
var playAgain,playAgainI,wellDone,wellDoneI;

function preload(){
    buddyIMG=loadImage("Buddy.png")
    BoxIMG=loadImage("cartin.jpg")
    GunI=loadImage("point1.png")
    GunI2=loadImage("point2.png")
    GunI3=loadImage("point3.png")
    Egun=loadImage("EGun.png")
    ak47I2=loadImage("ak47.png")
    Gs1=loadSound("12-Gauge-Pump-Action-Shotgun-Close-Gunshot-A-www.fesliyanstudios.com (1).mp3")
    BSImg=loadImage("bulls.png")
    MpI=loadImage("Mpointer.png")
    Pimg=loadImage("MPX.png")
    BImg=loadImage("tv.png")
    GTI=loadImage("GT1.png")
    BGI=loadImage("kkkk.jpg")
    StI=loadImage("StartB.png")
    Gs2=loadSound("Gun Silencer-SoundBible.com-193331132.mp3")
    EsI=loadImage("Es.png")
    Ps=loadSound("starting_pistol-Stephan_Schutze-613594351.mp3")
    cartI=loadImage("basket-full-icon.png")
    BombImg=loadImage("Sbomb.png")
    BombImg2=loadImage("Eexplore.png")
    slapI=loadImage("Slap.png")
    slapS=loadSound("Slap-SoundMaster13-49669815.mp3")
    liveI=loadImage("Rect.png")
    GskillI=loadImage("tskill.png")
    heart2I=loadImage("heart2.png")
    playAgainI=loadImage("play_again.png")
    wellDoneI=loadImage("well_done.png")

}




function setup(){
    var canvas = createCanvas(1000,600);
    engine = Engine.create();
    world = engine.world;

    ground =createSprite(500,600,1000,8)
    wall1 = createSprite(0,300,8,600)
    wall2 = createSprite(1000,300,8,600)
    wall3 =createSprite(500,0,1000,8)

    cart=createSprite(110,150,100,100)
    cart.addImage(cartI)
       cart.scale=0.2;

    buddy=createSprite(500,300,140,200)
    buddy.addImage(buddyIMG)
    buddy.scale=1.5;
  




   
    Gun=createSprite(200,200,10,10)
    Gun.addImage(GunI)
    Gun.scale=0.1;
  

    GunG=createGroup()
    GunG.add(Gun)

    Board=createSprite(540,320,100,100)
    Board.addImage(BImg)
    Board.scale=1.3;

 
   
  
 


  ak472=createSprite(320,320,10,10)
  ak472.addImage(ak47I2)
  ak472.scale=0.2;
 

  ak47G2=createGroup()
  ak47G2.add(ak472)

 EG=createSprite(530,320,10,10)
 EG.addImage(Egun)
 EG.scale=0.2;


 EgG=createGroup()
 EgG.add(EG)


 Pistol=createSprite(320,420,10,10)
 Pistol.addImage(Pimg)
 Pistol.scale=0.2;


 PistolG=createGroup()
 PistolG.add(Pistol)

 
   BombG=createGroup()
   

   slap=createSprite(200,200,10,10)
   slap.addImage(slapI)
   slap.scale=0.1;

   slaps=createSprite(705,420,10,10)
   slaps.addImage(slapI)
   slaps.scale=0.2;

   live=createSprite(800,50,100,20)
   live.shapeColor="green";

    L2=createSprite(800,50,100,20)
    L2.addImage(liveI)
    L2.scale=0.2;

    skill=createSprite(750,100,1,20)
    skill.shapeColor="blue";

    L3=createSprite(800,100,100,20)
    L3.addImage(liveI)
    L3.scale=0.2;

   stickbomb=createSprite(705,320,10,10)
 stickbomb.addImage(BombImg)
   stickbomb.scale=0.2;
  
   Gskill=createSprite(710,100,10,10)
   Gskill.addImage(GskillI)
   Gskill.scale=0.1;
 
   heart2=createSprite(710,50,10,10)
   heart2.addImage(heart2I)
   heart2.scale=0.07;



 GT=createSprite(500,190,10,10)
 GT.addImage(GTI)
 GT.scale=0.9;

 St=createSprite(500,440,10,10)
 St.addImage(StI)
 St.scale=0.5;


 playAgain=createSprite(110,150,10,10)
 playAgain.addImage(playAgainI)
 playAgain.scale=0.05;

 wellDone=createSprite(500,300,10,10)
 wellDone.addImage(wellDoneI)
 wellDone.scale=1.6;


  MP=createSprite(500,400,1000,8)
  MP.addImage(MpI)
  MP.scale=0.1;



}

function draw(){
    
   

    if(chooseState===0){
        background(BGI);
        skill.visible=false;
        cart.visible=false;
        stickbomb.visible=false;
        playAgain.visible=false;
        slap.visible=false;
        EG.visible=false;
        live.visible=false;
        buddy.visible=false;
        Gun.visible=false;
        ak472.visible=false;
        MP.visible=true;
        Pistol.visible=false;
        GT.visible=false;
        Board.visible=false;
        Gskill.visible=false;
        heart2.visible=false;
        wellDone.visible=false;
        St.visible=true;
        slaps.visible=false;
        L2.visible=false;
        L3.visible=false;
        MP.x=mouseX;
        MP.y=mouseY; 

        if(mousePressedOver(St)) {
    
            chooseState=1;
           
        }

      




    }


    



    if(chooseState===1){
        //6 weapons
        background(BoxIMG);

        cart.visible=true;
   

        skill.visible=false;
        playAgain.visible=false;

        slap.visible=false;
        live.visible=false;
        L3.visible=false;
        heart2.visible=false;

        L2.visible=false;
        stickbomb.visible=true;
        MP.visible=true;
        EG.visible=true;
        Pistol.visible=true;
        slaps.visible=true;
        Gskill.visible=false;
        wellDone.visible=false;

        buddy.visible=false;
        Gun.visible=false;
        ak472.visible=true;
      
        GT.visible=true;
        St.visible=false;

        Board.visible=true;
        MP.x=mouseX;
        MP.y=mouseY; 

       
        if(mousePressedOver(ak472)) {
    
            chooseState=2;
            
   
        }

        if(mousePressedOver(EG)) {
    
            chooseState=3;
   
        }

        if(mousePressedOver(Pistol)) {
    
            chooseState=4;
   
        }

        if(mousePressedOver(stickbomb)) {
    
            chooseState=5;
   
        }

        if(mousePressedOver(slaps)) {
    
            chooseState=6;
   
        }


        buddy.bounceOff(ground)
   buddy.bounceOff(wall1)
   buddy.bounceOff(wall2)
   buddy.bounceOff(wall3)

       
     buddy.rotation=buddy.rotation+8;


   
    Engine.update(engine);
    
   

   if(mousePressedOver(buddy)) {
    
     
      buddy.velocityX=Math.round(random(-12,12))
      buddy.velocityY=Math.round(random(-12,12))
   
    

      
     }


    }

    if(chooseState===2){

        // state for AK 47
        background(BoxIMG);
        cart.visible=true;
        Gun.addImage(GunI)
        L2.visible=true;
        Gun.x=mouseX;
        Gun.y=mouseY;
        EG.visible=false;
        Pistol.visible=false;
        stickbomb.visible=false;
        slap.visible=false;
        slaps.visible=false;
        live.visible=true;
        L3.visible=true;
        Gskill.visible=true;
        skill.visible=true;
        heart2.visible=true;
        playAgain.visible=false;
        wellDone.visible=false;

    buddy.visible=true;
    Gun.visible=true;
        ak472.visible=false;
        MP.visible=false;
      
        GT.visible=false;
        St.visible=false;
        Board.visible=false;


   buddy.bounceOff(ground)
   buddy.bounceOff(wall1)
   buddy.bounceOff(wall2)
   buddy.bounceOff(wall3)

       
     buddy.rotation=buddy.rotation+8;


   
    Engine.update(engine);
    
   

   if(mousePressedOver(buddy)) {
      Gs1.play()
     
      buddy.velocityX=Math.round(random(-12,12))
      buddy.velocityY=Math.round(random(-12,12))
      live.width=live.width-0.2;
      live.x=live.x-0.1;
     
      Lives=Lives-0.2;
      skill.width=skill.width+0.2;
    skill.x=skill.x+0.1;
  

        Bs = createSprite(mouseX,mouseY,10,40);
        Bs.addImage(BSImg)  
        Bs.scale = 0.2;
        Bs.lifetime =2;

     
      
     }
    
     if(mousePressedOver(cart)) {
    
        chooseState=1;

    }




    }
    
    if(chooseState===3){
       // state for Electric gun
        background(BoxIMG);
        EG.visible=false;
        Gun.addImage(GunI3)
        L2.visible=true;
        Gun.x=mouseX;
        Gun.y=mouseY;
        Pistol.visible=false;
        Gskill.visible=true;
        heart2.visible=true;
        playAgain.visible=false;
        wellDone.visible=false;

        cart.visible=true;
        stickbomb.visible=false;
        slap.visible=false;
        slaps.visible=false;
        live.visible=true;
        skill.visible=true;
        L3.visible=true;
    buddy.visible=true;
    Gun.visible=true;
        ak472.visible=false;
        MP.visible=false;
      
        GT.visible=false;
        St.visible=false;
        Board.visible=false;


   buddy.bounceOff(ground)
   buddy.bounceOff(wall1)
   buddy.bounceOff(wall2)
   buddy.bounceOff(wall3)

       
     buddy.rotation=buddy.rotation+8;


   
    Engine.update(engine);
    
   

   if(mousePressedOver(buddy)) {
      Gs2.play()
      live.width=live.width-0.2;
      live.x=live.x-0.1;
     
      Lives=Lives-0.2;
      skill.width=skill.width+0.2;
      skill.x=skill.x+0.1;
    
      buddy.velocityX=Math.round(random(-12,12))
      buddy.velocityY=Math.round(random(-12,12))
   
      Es = createSprite(mouseX,mouseY,10,40);
      Es.addImage(EsI)  
      Es.scale = 0.2;
      Es.lifetime =2;

      
     }
     if(mousePressedOver(cart)) {
    
        chooseState=1;

    }


    }

    if(chooseState===4){
        // state for pistol
         background(BoxIMG);
        cart.visible=true;
         EG.visible=false;
         Gun.addImage(GunI2)
         Gun.x=mouseX;
         Gun.y=mouseY;
        Gskill.visible=true;
        heart2.visible=true;
        playAgain.visible=false;
        wellDone.visible=false;

         Pistol.visible=false;
         stickbomb.visible=false;
         slap.visible=false;
         slaps.visible=false;
         skill.visible=true;
         L2.visible=true;
         live.visible=true;
         L3.visible=true;
     buddy.visible=true;
     Gun.visible=true;
         ak472.visible=false;
         MP.visible=false;
       
         GT.visible=false;
         St.visible=false;
         Board.visible=false;
 
 
    buddy.bounceOff(ground)
    buddy.bounceOff(wall1)
    buddy.bounceOff(wall2)
    buddy.bounceOff(wall3)
 
        
      buddy.rotation=buddy.rotation+8;
 
 
    
     Engine.update(engine);
     
    
 
    if(mousePressedOver(buddy)) {
       Ps.play()
       live.width=live.width-0.2;
       live.x=live.x-0.1;
      
       Lives=Lives-0.2;
       skill.width=skill.width+0.2;
       skill.x=skill.x+0.1;
     
       buddy.velocityX=Math.round(random(-12,12))
       buddy.velocityY=Math.round(random(-12,12))
    
         
 
       
      }
 
      if(mousePressedOver(cart)) {
    
        chooseState=1;

    }
     }



if(chooseState===5){
    // state for pistol
     background(BoxIMG);
     stickbomb.visible=false;
     slap.visible=false;
     slaps.visible=false;
        skill.visible=true;
        L2.visible=true;
    cart.visible=true;
     EG.visible=false;
     Gun.addImage(GunI)
     Gun.x=mouseX;
     Gun.y=mouseY;
     Pistol.visible=false;
     heart2.visible=true;
     playAgain.visible=false;
     wellDone.visible=false;

     live.visible=true;
     L3.visible=true;
 buddy.visible=true;
 Gun.visible=true;
     ak472.visible=false;
     MP.visible=false;
     Gskill.visible=true;
   
     GT.visible=false;
     St.visible=false;
     Board.visible=false;


buddy.bounceOff(ground)
buddy.bounceOff(wall1)
buddy.bounceOff(wall2)
buddy.bounceOff(wall3)

    
  buddy.rotation=buddy.rotation+8;

  if (BombG.isTouching(buddy)) {
    live.width=live.width-0.2;
    live.x=live.x-0.1;
   
    Lives=Lives-0.2;
    skill.width=skill.width+0.2;
    skill.x=skill.x+0.1;
  


    Gs1.play()
    BombG.setLifetimeEach(0);
   buddy2=createSprite(buddy.x,buddy.y,140,200)
   
   buddy2.addImage(BombImg2)
   buddy2.scale=2;
   buddy2.lifetime=5;
  
    buddy.velocityX=Math.round(random(-12,12))
       buddy.velocityY=Math.round(random(-12,12))
   }

   

 Engine.update(engine);
 
 BombG.bounceOff(ground)
 BombG.bounceOff(wall1)
 BombG.bounceOff(wall2)
 BombG.bounceOff(wall3)

if(mouseWentDown("leftButton")) { 
    spawnBombs()
    
}

 




    if(mousePressedOver(cart)) {
    
        chooseState=1;
    
    }
 }

 

 if(chooseState===1) {
    BombG.setLifetimeEach(0);
    
    }
    if(chooseState===2) {
        BombG.setLifetimeEach(0);
        
        } if(chooseState===3) {
            BombG.setLifetimeEach(0);
            
            } if(chooseState===4) {
                BombG.setLifetimeEach(0);
                
                }

                if(chooseState===6) {
                    BombG.setLifetimeEach(0);
                    }

                if(chooseState===6){
        
                     background(BoxIMG);
                    cart.visible=true;
                     EG.visible=false;
                     slap.x=mouseX;
                     slap.y=mouseY;
                     Pistol.visible=false;
                     stickbomb.visible=false;
                     slap.visible=true;
                 live.visible=true;
                 L2.visible=true;
                slaps.visible=false;
                L3.visible=true;
                 buddy.visible=true;
                heart2.visible=true;
                skill.visible=true;
                playAgain.visible=false;
                wellDone.visible=false;

                 Gun.visible=false;
                     ak472.visible=false;
                     MP.visible=false;
                     Gskill.visible=true;
                   
                     GT.visible=false;
                     St.visible=false;
                     Board.visible=false;
             
             
                buddy.bounceOff(ground)
                buddy.bounceOff(wall1)
                buddy.bounceOff(wall2)
                buddy.bounceOff(wall3)
             
                    
                  buddy.rotation=buddy.rotation+8;
             
             
                
                 Engine.update(engine);
                 
                
             
                if(mousePressedOver(buddy)) {
                    slapS.play()
                    live.width=live.width-0.2;
      live.x=live.x-0.1;
     
      Lives=Lives-0.2;
      skill.width=skill.width+0.2;
      skill.x=skill.x+0.1;
      Skills=Skills-0.2;
                   buddy.velocityX=Math.round(random(-12,12))
                   buddy.velocityY=Math.round(random(-12,12))
                
                     
             
                   
                  }
             
                  if(mousePressedOver(cart)) {
                
                    chooseState=1;
            
                }
                 }


                 if(live.width<0){
                live.width=live.width+100       
                   live.x=800;
                 Lives=Lives+100;
                 chooseState=7;
       

                }


                if(live.width>70){
                    live.shapeColor="green";
                  }

                if(live.width<70){
                    live.shapeColor="yellow";
                  }

                  if(live.width<20){
                    live.shapeColor="red";
                  }

                  if(skill.x>800){
                    skill.width=live.width-99        
                    skill.x=750;
                  
                  }

                  if(chooseState===7){
        
                    background(BoxIMG);
                   cart.visible=false;
                    EG.visible=false;
                    MP.x=mouseX;
                    MP.y=mouseY;
                    Pistol.visible=false;
                    stickbomb.visible=false;
                    slap.visible=false;
                live.visible=false;
                L2.visible=false;
               slaps.visible=false;
               L3.visible=false;
                buddy.visible=false;
               heart2.visible=false;
               skill.visible=false;
               playAgain.visible=true;
               wellDone.visible=true;

                Gun.visible=false;
                    ak472.visible=false;
                    MP.visible=true;
                    Gskill.visible=false;
                  
                    GT.visible=false;
                    St.visible=false;
                    Board.visible=false;
            
            
               buddy.bounceOff(ground)
               buddy.bounceOff(wall1)
               buddy.bounceOff(wall2)
               buddy.bounceOff(wall3)
            
                   
                 buddy.rotation=buddy.rotation+8;
            
            
               
                Engine.update(engine);
                
               
            
               if(mousePressedOver(playAgain)) {
            
               
                  chooseState=1;
            
                  
                 }
                }
    drawSprites()
}

function spawnBombs() {
    Bomb=createSprite(mouseX,mouseY,10,10)
   Bomb.addImage(BombImg)
   Bomb.scale=0.06;
   Bomb.rotation=Bomb.rotation+8;
   Bomb.velocityX=Math.round(random(-12,12))
   Bomb.velocityY=Math.round(random(-12,12))

   
 
   BombG.add(Bomb)
   
  
  
}
