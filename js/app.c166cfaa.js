(function(e){function t(t){for(var r,n,i=t[0],l=t[1],c=t[2],d=0,p=[];d<i.length;d++)n=i[d],Object.prototype.hasOwnProperty.call(s,n)&&s[n]&&p.push(s[n][0]),s[n]=0;for(r in l)Object.prototype.hasOwnProperty.call(l,r)&&(e[r]=l[r]);u&&u(t);while(p.length)p.shift()();return o.push.apply(o,c||[]),a()}function a(){for(var e,t=0;t<o.length;t++){for(var a=o[t],r=!0,i=1;i<a.length;i++){var l=a[i];0!==s[l]&&(r=!1)}r&&(o.splice(t--,1),e=n(n.s=a[0]))}return e}var r={},s={app:0},o=[];function n(t){if(r[t])return r[t].exports;var a=r[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,n),a.l=!0,a.exports}n.m=e,n.c=r,n.d=function(e,t,a){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(n.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)n.d(a,r,function(t){return e[t]}.bind(null,r));return a},n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="/Trello-Sierra/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=t,i=i.slice();for(var c=0;c<i.length;c++)t(i[c]);var u=l;o.push([0,"chunk-vendors"]),a()})({0:function(e,t,a){e.exports=a("56d7")},"56d7":function(e,t,a){"use strict";a.r(t);a("e260"),a("e6cf"),a("cca6"),a("a79d");var r=a("2b0e"),s=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-app",[a("AppBar"),a("v-main",[a("router-view")],1)],1)},o=[],n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-app-bar",{attrs:{app:"",color:"primary",dark:""}},[a("router-link",{staticClass:"white--text",attrs:{to:"/"}},[a("div",{staticClass:"d-flex"},[a("v-img",{staticClass:"shrink mr-2",attrs:{alt:"Vuetify Logo",contain:"",src:"https://logodix.com/logo/1144058.png",transition:"scale-transition",width:"40",height:"40"}}),a("span",{staticClass:"text-h4"},[e._v("BetterTrello")])],1)]),a("v-spacer"),this.$store.getters.isLogged?a("div",[a("v-btn",{attrs:{text:""},on:{click:e.logout}},[a("span",[e._v("Logout")])])],1):a("div",[a("v-btn",{staticClass:"mr-2",attrs:{to:"/login",text:""}},[a("span",[e._v("Login")])]),a("v-btn",{attrs:{to:"/register",text:""}},[a("span",[e._v("Register")])])],1)],1)},i=[],l={methods:{logout:function(){console.log("logout"),this.$store.dispatch("logout")}}},c=l,u=a("2877"),d=a("6544"),p=a.n(d),m=a("40dc"),f=a("8336"),v=a("adda"),h=a("2fa4"),b=Object(u["a"])(c,n,i,!1,null,null,null),g=b.exports;p()(b,{VAppBar:m["a"],VBtn:f["a"],VImg:v["a"],VSpacer:h["a"]});a("a717");var w={name:"Trello",components:{AppBar:g},data:function(){return{}}},y=w,V=a("7496"),x=a("f6c4"),k=Object(u["a"])(y,s,o,!1,null,null,null),_=k.exports;p()(k,{VApp:V["a"],VMain:x["a"]});var C=a("8c4f"),j=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-container",[a("v-row",{attrs:{justify:"center mt-6"}},[a("v-img",{attrs:{height:"300",src:"https://avatars.slack-edge.com/2021-07-19/2282472048054_9a51d280179d828b3ad7_512.png",transition:"scale-transition",contain:""}})],1),a("v-row",{attrs:{justify:"center"}},[a("h1",[e._v("Welcome on Trello!")])]),a("v-row",{attrs:{justify:"center"}},[a("h3",[e._v("Better Trello")])])],1)},P=[],R={},S=R,T=a("a523"),O=a("0fd9"),$=Object(u["a"])(S,j,P,!1,null,null,null),E=$.exports;p()($,{VContainer:T["a"],VImg:v["a"],VRow:O["a"]});var M=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-container",{attrs:{fluid:""}},[a("v-row",{staticClass:"mt-5 mb-12",attrs:{align:"center",justify:"center"}},[a("v-col",{attrs:{cols:"12",md:"6",align:"center",justify:"center"}},[a("lottie-player",{staticStyle:{width:"70%"},attrs:{src:"https://assets7.lottiefiles.com/packages/lf20_87uabjh2.json",background:"transparent",speed:"1",loop:"",autoplay:""}})],1),a("v-col",{attrs:{cols:"12",md:"6"}},[a("v-layout",{attrs:{"align-center":"","justify-center":""}},[a("v-flex",[a("v-card",{staticClass:"elevation-4 mt-12 ml-6 mr-6"},[a("v-toolbar",{attrs:{dark:"",color:"primary"}},[a("v-toolbar-title",[e._v("Login")])],1),a("v-card-text",{staticClass:"px-8"},[a("v-form",{ref:"form",attrs:{validation:""},model:{value:e.isValid,callback:function(t){e.isValid=t},expression:"isValid"}},[a("v-text-field",{attrs:{"prepend-icon":"mdi-at",name:"email",label:"Email",type:"text",clearable:"",rules:e.emailRules,required:""},model:{value:e.email,callback:function(t){e.email=t},expression:"email"}}),a("v-text-field",{attrs:{id:"password","prepend-icon":"mdi-lock",name:"password",label:"Password",type:"password",clearable:"",rules:e.passwordRules,required:""},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}}),a("v-switch",{attrs:{label:"Remember Me"},model:{value:e.rememberMe,callback:function(t){e.rememberMe=t},expression:"rememberMe"}})],1),a("div",{staticClass:"mt-4"},[a("span",{staticClass:"red--text"},[e._v(e._s(e.error))])])],1),a("v-card-actions",{staticClass:"pa-5"},[a("v-spacer"),a("v-btn",{staticClass:"mr-6",attrs:{fab:"",color:"#E57373",dark:""},on:{click:e.resetClicked}},[a("v-icon",[e._v("mdi-backspace")])],1),a("v-btn",{attrs:{fab:"",color:"green",disabled:!e.isValid},on:{click:e.loginClicked}},[a("v-icon",{attrs:{dark:""}},[e._v("mdi-arrow-right")])],1)],1)],1)],1)],1)],1)],1)],1)},B=[],L={data:function(){return{email:"",password:"",rememberMe:!1,isValid:!1,error:"",emailRules:[function(e){return!!e||"Email is required"}],passwordRules:[function(e){return!!e||"Password is required"}]}},methods:{loginClicked:function(){this.$refs.form.validate()&&this.login(this.email,this.password,this.rememberMe)},login:function(e,t,a){var r=this,s={email:e,password:t,rememberMe:a};this.$store.dispatch("login",s).catch((function(e){r.error="Invalid email or password"}))},resetClicked:function(){this.$refs.form.reset()}}},q=L,F=a("b0af"),I=a("99d9"),A=a("62ad"),U=a("0e8f"),D=a("4bd4"),J=a("132d"),z=a("a722"),H=a("b73d"),K=a("8654"),W=a("71d9"),Y=a("2a7f"),G=Object(u["a"])(q,M,B,!1,null,null,null),N=G.exports;p()(G,{VBtn:f["a"],VCard:F["a"],VCardActions:I["a"],VCardText:I["b"],VCol:A["a"],VContainer:T["a"],VFlex:U["a"],VForm:D["a"],VIcon:J["a"],VLayout:z["a"],VRow:O["a"],VSpacer:h["a"],VSwitch:H["a"],VTextField:K["a"],VToolbar:W["a"],VToolbarTitle:Y["a"]});var Q=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-container",{attrs:{fluid:""}},[a("v-row",{staticClass:"mt-5 mb-12",attrs:{align:"center",justify:"center"}},[a("v-col",{attrs:{cols:"12",md:"6",align:"center",justify:"center"}},[a("lottie-player",{staticStyle:{width:"70%"},attrs:{src:"https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json",background:"transparent",speed:"1",loop:"",autoplay:""}})],1),a("v-col",{attrs:{cols:"12",md:"6"}},[a("v-layout",{attrs:{"align-center":"","justify-center":""}},[a("v-flex",[a("v-card",{staticClass:"elevation-4 mt-12 ml-6 mr-6"},[a("v-toolbar",{attrs:{dark:"",color:"primary"}},[a("v-toolbar-title",[e._v("Register")])],1),a("v-card-text",{staticClass:"px-8"},[a("v-form",{ref:"form",attrs:{validation:""},model:{value:e.isValid,callback:function(t){e.isValid=t},expression:"isValid"}},[a("v-text-field",{attrs:{"prepend-icon":"mdi-at",name:"email",label:"Email",type:"text",rules:e.emailRules,clearable:"",required:""},model:{value:e.email,callback:function(t){e.email=t},expression:"email"}}),a("v-text-field",{attrs:{id:"password","prepend-icon":"mdi-lock",name:"password",label:"Password",type:"password",rules:e.passwordRules,clearable:"",required:""},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}}),a("v-text-field",{attrs:{id:"repeated","prepend-icon":"mdi-lock-check",name:"repeated",label:"Password",type:"password",rules:e.repeatedPasswordRules,clearable:"",required:""},model:{value:e.repeatedPassword,callback:function(t){e.repeatedPassword=t},expression:"repeatedPassword"}})],1),a("div",{staticClass:"mt-4"},[a("span",{staticClass:"red--text"},[e._v(e._s(e.error))])])],1),a("v-card-actions",{staticClass:"pa-5"},[a("v-spacer"),a("v-btn",{staticClass:"mr-6",attrs:{fab:"",color:"#E57373",dark:""},on:{click:e.resetClicked}},[a("v-icon",[e._v("mdi-backspace")])],1),a("v-btn",{attrs:{fab:"",color:"green",disabled:!e.isValid},on:{click:e.registerClicked}},[a("v-icon",{attrs:{dark:""}},[e._v("mdi-arrow-right")])],1)],1)],1)],1)],1)],1)],1)],1)},X=[],Z=(a("ac1f"),a("00b4"),{data:function(){var e=this;return{email:"",password:"",repeatedPassword:"",isValid:!1,error:"",emailRules:[function(e){return!!e||"Email is required"},function(e){return/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(e)||"E-mail must be valid"}],passwordRules:[function(e){return e.length>=8||"Password must have at lest 8 characters"}],repeatedPasswordRules:[function(e){return!!e||"Repeated password is required"},function(t){return t==e.password||"Passwords are not the same"}]}},methods:{registerClicked:function(){this.$refs.form.validate()&&this.register(this.email,this.password)},register:function(e,t){var a=this,r={email:e,password:t};this.$store.dispatch("register",r).catch((function(e){a.error="User with provided email address already exists"}))},resetClicked:function(){this.$refs.form.reset()}}}),ee=Z,te=Object(u["a"])(ee,Q,X,!1,null,null,null),ae=te.exports;p()(te,{VBtn:f["a"],VCard:F["a"],VCardActions:I["a"],VCardText:I["b"],VCol:A["a"],VContainer:T["a"],VFlex:U["a"],VForm:D["a"],VIcon:J["a"],VLayout:z["a"],VRow:O["a"],VSpacer:h["a"],VTextField:K["a"],VToolbar:W["a"],VToolbarTitle:Y["a"]});var re=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-container",[a("v-row",{attrs:{justify:"center mt-6"}},[a("lottie-player",{staticStyle:{width:"400px",height:"400px"},attrs:{src:"https://assets6.lottiefiles.com/packages/lf20_vmlm0zew.json",background:"transparent",speed:"1",autoplay:""}})],1),a("v-row",{attrs:{justify:"center"}},[a("h1",[e._v("You have been logged out!")])]),a("v-row",{attrs:{justify:"center"}},[a("v-btn",{staticClass:"mt-4",attrs:{to:"/",outlined:"",color:"indigo"}},[e._v("To home page")])],1)],1)},se=[],oe={},ne=oe,ie=Object(u["a"])(ne,re,se,!1,null,null,null),le=ie.exports;p()(ie,{VBtn:f["a"],VContainer:T["a"],VRow:O["a"]});var ce=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-container",[a("v-row",{staticClass:"mt-12",attrs:{justify:"center"}},[a("h1",[e._v("Boards")])]),a("v-row",{attrs:{justify:"center"}},[a("h3",[e._v("Here should be list of user boards")])])],1)},ue=[],de={},pe=de,me=Object(u["a"])(pe,ce,ue,!1,null,null,null),fe=me.exports;p()(me,{VContainer:T["a"],VRow:O["a"]}),r["a"].use(C["a"]);var ve=[{path:"/",name:"home",component:E},{path:"/login",name:"login",component:N},{path:"/register",name:"register",component:ae},{path:"/logout",name:"logout",component:le},{path:"/boards",name:"boards",component:fe,meta:{auth:!0}}];r["a"].router=new C["a"]({mode:"history",base:"/Trello-Sierra/",routes:ve});var he=r["a"].router,be=a("2f62"),ge=(a("d3b7"),a("b0c0"),{state:function(){return{}},actions:{fetch:function(e){return r["a"].auth.fetch(e)},login:function(e,t){var a=r["a"].auth.redirect();return new Promise((function(e,s){r["a"].auth.login({data:{email:t.email,password:t.password},redirect:{name:a?a.from.name:"boards"},staySignedIn:t.rememberMe}).then(e,s)}))},register:function(e,t){return t=t||{},new Promise((function(a,s){r["a"].auth.register({data:{email:t.email,password:t.password},redirect:null,staySignedIn:!0,autoLogin:!1,fetchUser:!0}).then((function(r){t.rememberMe=!1,e.dispatch("login",t).then(a,s)}),s)}))},logout:function(e){return r["a"].auth.logout({redirect:"logout"})}},getters:{user:function(){return r["a"].auth.user()},isLogged:function(){return null!=r["a"].auth.user()}}});r["a"].use(be["a"]);var we=new be["a"].Store({modules:{auth:ge}}),ye=a("f309");r["a"].use(ye["a"]);var Ve=new ye["a"]({}),xe=a("bc3a"),ke=a.n(xe),_e=a("130e");ke.a.defaults.baseURL="https://pawtrello.herokuapp.com",r["a"].use(_e["a"],ke.a);var Ce={root:"https://pawtrello.herokuapp.com"},je=a("67a9"),Pe=a("9504"),Re=a("b251"),Se=a("59a5"),Te=a("45c0"),Oe=a("6f51");Te["a"].params.client_id="547886745924-4vrbhl09fr3t771drtupacct6f788566.apps.googleusercontent.com",Oe["a"].params.client_id="196729390739201",r["a"].use(je["a"],{plugins:{http:r["a"].axios,router:r["a"].router},drivers:{auth:Pe["a"],http:Re["a"],router:Se["a"],oauth2:{google:Te["a"],facebook:Oe["a"]}},options:{rolesKey:"type",notFoundRedirect:{name:"user-account"},parseUserData:function(e){return e},refreshData:{enabled:!1,interval:0}}});var $e={};a("5aea");r["a"].config.productionTip=!1,new r["a"]({el:"#app",http:Ce,router:he,store:we,vuetify:Ve,config:$e,render:function(e){return e(_)},created:function(){if(sessionStorage.redirect){var e=sessionStorage.redirect;delete sessionStorage.redirect,this.$router.push(e)}}})},"5aea":function(e,t,a){}});
//# sourceMappingURL=app.c166cfaa.js.map