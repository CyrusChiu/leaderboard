(function(t){function e(e){for(var a,s,i=e[0],c=e[1],u=e[2],p=0,f=[];p<i.length;p++)s=i[p],Object.prototype.hasOwnProperty.call(r,s)&&r[s]&&f.push(r[s][0]),r[s]=0;for(a in c)Object.prototype.hasOwnProperty.call(c,a)&&(t[a]=c[a]);l&&l(e);while(f.length)f.shift()();return o.push.apply(o,u||[]),n()}function n(){for(var t,e=0;e<o.length;e++){for(var n=o[e],a=!0,i=1;i<n.length;i++){var c=n[i];0!==r[c]&&(a=!1)}a&&(o.splice(e--,1),t=s(s.s=n[0]))}return t}var a={},r={app:0},o=[];function s(e){if(a[e])return a[e].exports;var n=a[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.m=t,s.c=a,s.d=function(t,e,n){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)s.d(n,a,function(e){return t[e]}.bind(null,a));return n},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],c=i.push.bind(i);i.push=e,i=i.slice();for(var u=0;u<i.length;u++)e(i[u]);var l=c;o.push([0,"chunk-vendors"]),n()})({0:function(t,e,n){t.exports=n("56d7")},"034f":function(t,e,n){"use strict";n("85ec")},"0646":function(t,e,n){},"56d7":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var a=n("2b0e"),r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"app"}},[t._m(0),n("div",{staticStyle:{position:"relative"}},[n("div",{attrs:{id:"background-extension"}}),n("div",{staticClass:"CompetitorList"},[t._m(1),n("transition-group",{key:t.show,attrs:{appear:"","enter-active-class":"animated flipInX","leave-active-class":"animated fadeOutLeft"}},t._l(t.testdata,(function(t,e){return n("DashBoard",{key:e,attrs:{data:t,rank:e}})})),1)],1)]),n("button",{on:{click:t.updateData}},[t._v(" Toggle render ")])])},o=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("nav",[a("img",{attrs:{src:n("e4fe")}})])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"Header"},[a("h1",{staticClass:"Header__title"},[t._v("# Ranking")]),a("img",{staticClass:"Header__image",attrs:{src:n("d57f")}})])}],s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"Athlete animated"},[n("div",{staticClass:"Athlete__rank"},[n("h5",[t._v(" "+t._s(t.rank+1)+" ")])]),n("img",{staticClass:"avator",attrs:{src:t.avator[t.stringToNum(t.data.user_name)%6]}}),n("h2",{staticClass:"Athlete__name"},[t._v(t._s(t.data.user_name))]),n("h4",{staticClass:"Athlete__reps"},[t._v(" "+t._s(t.data.score)+" ")])])},i=[],c=(n("159b"),n("ac1f"),n("1276"),{name:"Dashboard",props:["data","show","rank"],methods:{stringToNum:function(t){var e=0;return t.toUpperCase().split("").forEach((function(t){e+=t.charCodeAt(0)-64})),e}},data:function(){return{avator:["https://image.flaticon.com/icons/png/128/4322/4322992.png","https://image.flaticon.com/icons/png/128/4322/4322991.png","https://image.flaticon.com/icons/png/128/3940/3940403.png","https://image.flaticon.com/icons/png/128/3940/3940404.png","https://image.flaticon.com/icons/png/128/3940/3940402.png","https://image.flaticon.com/icons/png/128/3940/3940401.png"]}}}),u=c,l=(n("824f"),n("2877")),p=Object(l["a"])(u,s,i,!1,null,null,null),f=p.exports,d={name:"App",components:{DashBoard:f},mounted:function(){this.initWebSocket()},methods:{initWebSocket:function(){var t="ws://127.0.0.1:2700";this.websocket=new WebSocket(t),this.websocket.onmessage=this.websocketonmessage},websocketonmessage:function(t){console.log(t.data)},updateData:function(){this.show=!this.show,this.testdata=[{user_name:"daniel",score:10},{user_name:"kent",score:50},{user_name:"raix",score:30}].sort((function(t,e){return t.score<e.score?1:-1}))}},data:function(){return{websocket:null,show:!0,testdata:[]}}},h=d,m=(n("034f"),Object(l["a"])(h,r,o,!1,null,null,null)),g=m.exports;n("8672");a["a"].config.productionTip=!1,new a["a"]({render:function(t){return t(g)}}).$mount("#app")},"824f":function(t,e,n){"use strict";n("0646")},"85ec":function(t,e,n){},8672:function(t,e,n){},d57f:function(t,e,n){t.exports=n.p+"img/trophy.add13f86.svg"},e4fe:function(t,e,n){t.exports=n.p+"img/logoo.83f6599f.png"}});
//# sourceMappingURL=app.c18aa629.js.map