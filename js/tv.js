$(function(){
  for(i=0;i<4;i++){
    $('.buzz_wrapper .text span').eq(0).clone().prependTo('.buzz_wrapper .text');
  }
  for(i=0;i<4;i++){
    $('.nav-wrapper .text').eq(0).clone().prependTo('.nav-wrapper');
  }
  for(i=0;i<4;i++){
    $('.fancy-junk').eq(0).clone().prependTo('.cool-junk');
  }
  for(i=0;i<10;i++){
    $('.buzz_wrapper .scanline').eq(0).clone().appendTo('.buzz_wrapper');
  }
});
