(()=>{"use strict";var e=function(e,n){return Number(Math.round(e+"e"+n)+"e-"+n)},n=1.000336779605042,t=.0007486347018305433,r=document.querySelector("#generate"),u=document.querySelector("#utm_northing"),i=document.querySelector("#utm_eastings"),c=document.querySelector("#cassini_x"),o=document.querySelector("#cassini_y"),s=function(r,u){return{utm_eastings:e(n*r+t*u+277437.92231410294,3),utm_northing:e(t*r+n*u+10000217.281733181,3)}};r.addEventListener("click",(function(){!function(e,n){try{if(""==e||""==n)throw"An input for coordinates is empty";if(isNaN(e)||isNaN(n))throw"An input value is not a number";u.innerHTML=s(e,n).utm_northing,i.innerHTML=s(e,n).utm_eastings}catch(e){alert(e),document.querySelector("#cassini_x").value="",document.querySelector("#cassini_y").value=""}}(c.value,o.value)})),o.addEventListener("keypress",(function(){u.innerHTML=""})),c.addEventListener("keypress",(function(){i.innerHTML=""}))})();