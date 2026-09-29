import streamlit as st
import streamlit.components.v1 as components
import json

def apply_theme_and_cat(app_theme, current_cat_mode, is_equipped, library_files=None):
    if library_files is None:
        library_files = []
        
    files_json = json.dumps(library_files)
    is_neon = "Evori" in app_theme

    if app_theme == "Evori Neon (Pink)":
        c_pri, c_sec, c_glow = "#ff69b4", "#ff1493", "#ffb6c1"
        bg_main, bg_side = "#140510", "#24051a"
        cat_hue = "290deg"
    elif app_theme == "Evori Neon (Purple)":
        c_pri, c_sec, c_glow = "#d870ff", "#8a2be2", "#e066ff"
        bg_main, bg_side = "#0d0214", "#1a0524"
        cat_hue = "250deg"
    elif app_theme == "Evori Neon (Green)":
        c_pri, c_sec, c_glow = "#00ffaa", "#008855", "#55ffcc"
        bg_main, bg_side = "#02140a", "#052414"
        cat_hue = "100deg"
    elif app_theme == "Evori Neon (Orange)":
        c_pri, c_sec, c_glow = "#ffaa00", "#cc4400", "#ffcc55"
        bg_main, bg_side = "#140a02", "#241005"
        cat_hue = "340deg"
    else:
        c_pri, c_sec, c_glow, bg_main, bg_side, cat_hue = "#ff69b4", "#ff1493", "#ffb6c1", "#140510", "#24051a", "290deg"

    if is_neon:
        st.markdown(f"""
        <style>
        .stApp, [data-testid="stHeader"] {{ background-color: transparent !important; }}
        body, [data-testid="stAppViewContainer"] {{ background-color: {bg_main} !important; }}
        h1, h2, h3, .stMarkdown p, .stText, label {{ color: {c_pri} !important; text-shadow: 0 0 8px {c_sec}; }}
        .stButton > button {{ background-color: {bg_side} !important; color: {c_pri} !important; border: 1px solid {c_pri} !important; box-shadow: 0 0 10px {c_sec} !important; font-weight: bold; }}
        .stTextInput > div > div > input {{ color: {c_pri} !important; border: 1px solid {c_pri} !important; background-color: {bg_side} !important; box-shadow: 0 0 5px {c_sec} !important; }}
        .stSelectbox > div > div > div {{ color: {c_pri} !important; border: 1px solid {c_pri} !important; background-color: {bg_side} !important; box-shadow: 0 0 5px {c_sec} !important; }}
        [data-testid="stSidebar"] {{ background-color: rgba(20, 5, 25, 0.9) !important; border-right: 1px solid {c_pri}; box-shadow: 2px 0 15px {c_sec}; }}
        .stToast {{ background-color: {bg_side} !important; color: {c_pri} !important; border: 1px solid {c_pri} !important; }}
        </style>
        """, unsafe_allow_html=True)
        
        components.html(f"""
        <script>
            const parentDoc = window.parent.document;
            if (!parentDoc.getElementById('evori-neon-bg')) {{
                const bg = parentDoc.createElement('div'); bg.id = 'evori-neon-bg'; bg.style.position = 'fixed'; bg.style.top = '0'; bg.style.left = '0'; bg.style.width = '100vw'; bg.style.height = '100vh'; bg.style.pointerEvents = 'none'; bg.style.zIndex = '0'; parentDoc.body.appendChild(bg);
                const style = parentDoc.createElement('style');
                style.innerHTML = `
                    .evori-star {{ position: absolute; background: white; border-radius: 50%; box-shadow: 0 0 6px {c_glow}; animation: twinkle infinite alternate ease-in-out; }}
                    @keyframes twinkle {{ 0% {{ opacity: 0.1; transform: scale(0.8); }} 100% {{ opacity: 1; transform: scale(1.2); }} }}
                    .evori-bg-meteor {{ position: absolute; width: 3px; height: 90px; background: linear-gradient(to bottom, transparent, {c_sec}, #fff); filter: drop-shadow(0 0 8px {c_pri}); border-radius: 50%; }}
                    @keyframes fall-left {{ 0% {{ transform: translateY(-100px) rotate(45deg); opacity: 1; }} 100% {{ transform: translateY(120vh) translateX(-120vh) rotate(45deg); opacity: 0; }} }}
                    @keyframes fall-right {{ 0% {{ transform: translateY(-100px) rotate(-45deg); opacity: 1; }} 100% {{ transform: translateY(120vh) translateX(120vh) rotate(-45deg); opacity: 0; }} }}
                `;
                bg.appendChild(style);
                for(let i=0; i<80; i++) {{ let s = parentDoc.createElement('div'); s.className = 'evori-star'; s.style.width = (Math.random()*2.5 + 1) + 'px'; s.style.height = s.style.width; s.style.left = Math.random()*100 + 'vw'; s.style.top = Math.random()*100 + 'vh'; s.style.animationDuration = (Math.random()*3 + 1.5) + 's'; s.style.animationDelay = (Math.random()*2) + 's'; bg.appendChild(s); }}
                window.parent.neonMeteorLoop = setInterval(() => {{ if (Math.random() > 0.4) {{ let m = parentDoc.createElement('div'); m.className = 'evori-bg-meteor'; m.style.left = (Math.random()*100) + 'vw'; m.style.top = '-100px'; let dur = Math.random()*0.8 + 0.8; let dir = Math.random() > 0.5 ? 'fall-left' : 'fall-right'; m.style.animation = `${{dir}} ${{dur}}s linear forwards`; bg.appendChild(m); setTimeout(() => m.remove(), dur * 1000); }} }}, 2000);
            }} else {{
                const style = parentDoc.getElementById('evori-neon-bg').querySelector('style');
                if(style) {{ style.innerHTML = style.innerHTML.replace(/box-shadow: 0 0 6px .*?;/, `box-shadow: 0 0 6px {c_glow};`).replace(/background: linear-gradient\\(to bottom, transparent, .*, #fff\\);/, `background: linear-gradient(to bottom, transparent, {c_sec}, #fff);`).replace(/filter: drop-shadow\\(0 0 8px .*\\);/, `filter: drop-shadow(0 0 8px {c_pri});`); }}
            }}
        </script>
        """, height=0, width=0)
    else:
        components.html("""
        <script>
            const bg = window.parent.document.getElementById('evori-neon-bg'); if (bg) bg.remove();
            if (window.parent.neonMeteorLoop) clearInterval(window.parent.neonMeteorLoop);
        </script>
        """, height=0, width=0)

    if is_equipped:
        EVORI_HTML = """
        <script>
            const parentDoc = window.parent.document;
            const parentWin = window.parent;
            if (parentWin.evoriLoop) clearInterval(parentWin.evoriLoop);
            
            let oldPosX = window.parent.sessionStorage.getItem('evoriPosX') ? parseFloat(window.parent.sessionStorage.getItem('evoriPosX')) : 50;
            let oldFacingRight = window.parent.sessionStorage.getItem('evoriFacing') ? window.parent.sessionStorage.getItem('evoriFacing') === 'true' : true;
            let savedChatHtml = window.parent.sessionStorage.getItem('evoriChat') || '<div class="msg-cat">Meow! ✨ I am Evori! 🐾</div>';
            
            let existingCat = parentDoc.getElementById('evori-cat-companion'); let existingBox = parentDoc.getElementById('evori-chatbox');
            if (existingCat && parentWin.evoriState) { oldPosX = parentWin.evoriState.posX; oldFacingRight = parentWin.evoriState.facingRight; existingCat.remove(); }
            if (existingBox) { let chatContent = existingBox.querySelector('#chat-content'); if (chatContent) savedChatHtml = chatContent.innerHTML; existingBox.remove(); }
            let oldStyles = parentDoc.getElementById('evori-cat-styles'); if (oldStyles) oldStyles.remove();

            const libraryFiles = {FILES_JSON};

            const style = parentDoc.createElement('style'); style.id = 'evori-cat-styles';
            style.innerHTML = `
                :root { --evori-pri: {C_PRI}; --evori-sec: {C_SEC}; --evori-glow: {C_GLOW}; --evori-bg: {BG_SIDE}; --evori-hue: {CAT_HUE}; }
                #evori-cat-companion { position: fixed; bottom: 20px; left: 50px; width: 80px; height: 80px; z-index: 2147483647 !important; pointer-events: auto; cursor: pointer; transition: transform 0.2s, bottom 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); filter: drop-shadow(0 0 15px var(--evori-pri)) drop-shadow(0 0 30px var(--evori-sec)); user-select: none; }
                .cat-body { font-size: 55px; line-height: 80px; text-align: center; animation: float 3s ease-in-out infinite; transform-origin: center bottom; filter: sepia(0.5) saturate(3) hue-rotate(var(--evori-hue)); position: relative; }
                #evori-accessory { position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 2; }
                .cat-speech-bubble { position: absolute; bottom: 90px; left: 50%; transform: translateX(-50%); background: rgba(20, 20, 20, 0.9); border: 2px solid var(--evori-pri); color: #fff; padding: 8px 12px; border-radius: 12px; font-family: 'Segoe UI', sans-serif; font-size: 13px; font-weight: bold; white-space: nowrap; opacity: 0; transition: opacity 0.3s; pointer-events: none; box-shadow: 0 0 10px var(--evori-sec); z-index: 10; }
                .cat-speech-bubble::after { content: ''; position: absolute; bottom: -6px; left: 50%; margin-left: -6px; border-width: 6px 6px 0; border-style: solid; border-color: var(--evori-pri) transparent transparent transparent; }
                .particle { position: absolute; pointer-events: none; animation: fadeUp 1s forwards; z-index: 5; }
                .cat-meteor-trail { position: fixed; width: 14px; height: 60px; background: linear-gradient(to bottom, var(--evori-glow), var(--evori-sec), transparent); border-radius: 7px; pointer-events: none; z-index: 2147483645; animation: catMeteorFade 0.6s forwards ease-out; filter: drop-shadow(0 0 10px var(--evori-pri)) drop-shadow(0 0 20px var(--evori-sec)); }
                @keyframes catMeteorFade { 0% { opacity: 1; transform: scale(1) translateY(0); } 100% { opacity: 0; transform: scale(0.2) translateY(60px); } }
                @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
                @keyframes walk { 0%, 100% { transform: rotate(-5deg); } 50% { transform: rotate(5deg); } }
                @keyframes sleep { 0%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.85) translateY(5px); } }
                @keyframes fadeUp { 0% { opacity: 1; transform: translateY(0) scale(1); } 100% { opacity: 0; transform: translateY(-30px) scale(1.5); } }
                #evori-chatbox { position: fixed; bottom: 20px; right: 20px; width: 65px; height: 65px; background: rgba(14, 17, 23, 0.95); border: 2px solid var(--evori-pri); border-radius: 35px; z-index: 2147483646 !important; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 0 20px var(--evori-sec); }
                #evori-chatbox:hover, #evori-chatbox:focus-within { width: 320px; height: 400px; border-radius: 15px; }
                #chat-header { height: 65px; flex-shrink: 0; display: flex; align-items: center; justify-content: center; color: var(--evori-pri); font-size: 32px; font-weight: bold; transition: all 0.3s; cursor: pointer; }
                #evori-chatbox:hover #chat-header, #evori-chatbox:focus-within #chat-header { height: 40px; font-size: 16px; border-bottom: 1px solid var(--evori-sec); background: var(--evori-bg); }
                #chat-content { flex-grow: 1; padding: 10px; overflow-y: auto; display: flex; flex-direction: column; gap: 8px; opacity: 0; transition: opacity 0.2s; font-family: 'Segoe UI', sans-serif; font-size: 14px; scroll-behavior: smooth; }
                #evori-chatbox:hover #chat-content, #evori-chatbox:focus-within #chat-content { opacity: 1; }
                .msg-user { align-self: flex-end; background: var(--evori-pri); color: #111; padding: 8px 12px; border-radius: 15px 15px 0 15px; max-width: 80%; font-weight: bold; }
                .msg-cat { align-self: flex-start; background: #222; color: var(--evori-pri); padding: 8px 12px; border-radius: 15px 15px 15px 0; max-width: 80%; border: 1px solid var(--evori-sec); line-height: 1.4; word-wrap: break-word;}
                #chat-input-area { display: flex; padding: 10px; gap: 5px; opacity: 0; }
                #evori-chatbox:hover #chat-input-area, #evori-chatbox:focus-within #chat-input-area { opacity: 1; }
                #chat-input { flex-grow: 1; background: #111; border: 1px solid var(--evori-pri); color: white; border-radius: 15px; padding: 8px 12px; outline: none; }
                #chat-send { background: var(--evori-pri); color: #111; border: none; border-radius: 15px; padding: 0 12px; cursor: pointer; font-weight: bold; }
                #chat-content::-webkit-scrollbar { width: 5px; }
                #chat-content::-webkit-scrollbar-thumb { background: var(--evori-pri); border-radius: 5px; }
            `;
            parentDoc.head.appendChild(style);

            const catContainer = parentDoc.createElement('div'); catContainer.id = 'evori-cat-companion'; catContainer.dataset.mode = "{CAT_MODE}";
            const catBody = parentDoc.createElement('div'); catBody.className = 'cat-body'; catBody.id = 'evori-cat-body'; catBody.innerHTML = '🐱<div id="evori-accessory"></div>';
            const bubble = parentDoc.createElement('div'); bubble.className = 'cat-speech-bubble'; bubble.id = 'cat-speech'; bubble.innerHTML = 'Meow!';
            catContainer.appendChild(bubble); catContainer.appendChild(catBody); parentDoc.body.appendChild(catContainer);

            const chatbox = parentDoc.createElement('div'); chatbox.id = 'evori-chatbox';
            chatbox.innerHTML = `<div id="chat-header">💬</div><div id="chat-content">${savedChatHtml}</div><div id="chat-input-area"><input type="text" id="chat-input" placeholder="Chat with Evori..." autocomplete="off"/><button id="chat-send">Send</button></div>`;
            parentDoc.body.appendChild(chatbox);

            parentWin.evoriState = { posX: oldPosX, velocityX: 1.5, isIdle: false, isSleeping: false, facingRight: oldFacingRight, bubbleTimeout: null };
            catContainer.style.left = parentWin.evoriState.posX + 'px'; catBody.style.transform = parentWin.evoriState.facingRight ? 'scaleX(1)' : 'scaleX(-1)';

            function updateAccessory(mode) {
                const acc = parentDoc.getElementById('evori-accessory'); if (!acc) return;
                if (mode === "Strategist" || mode === "Finance") { acc.innerHTML = '<div style="font-size:38px; position:absolute; top:13px; width:100%; text-align:center; filter: drop-shadow(0 0 5px var(--evori-pri));">👓</div>'; }
                else if (mode === "CEO") { acc.innerHTML = '<div style="font-size:28px; position:absolute; top:42px; width:100%; text-align:center;">👔</div>'; }
                else if (mode === "Examiner") { acc.innerHTML = '<div style="font-size:45px; position:absolute; top:-15px; left:4px; width:100%; text-align:center;">🎓</div>'; }
                else { acc.innerHTML = ''; }
            }
            updateAccessory("{CAT_MODE}");

            parentWin.evoriActions = {
                speak: function(mode, overrideText) {
                    clearTimeout(parentWin.evoriState.bubbleTimeout);
                    bubble.innerHTML = overrideText || "Meow!";
                    bubble.style.opacity = 1;
                    parentWin.evoriState.bubbleTimeout = setTimeout(() => { bubble.style.opacity = 0; }, 3500);
                },
                createParticle: function(emoji) {
                    const p = parentDoc.createElement('div'); p.className = 'particle'; p.innerHTML = emoji;
                    p.style.left = (Math.random() * 40 + 10) + 'px'; p.style.bottom = '40px'; p.style.fontSize = (Math.random() * 10 + 12) + 'px';
                    catContainer.appendChild(p); setTimeout(() => p.remove(), 1000);
                },
                triggerKamikaze: function() {
                    parentWin.evoriState.isSleeping = false; parentWin.evoriActions.speak(null, "KAMIKAZEEE! 🚀🐱");
                    catContainer.style.transition = "all 0.6s ease-in"; catContainer.style.bottom = "120vh"; 
                    parentWin.evoriState.posX += (parentWin.evoriState.facingRight ? 500 : -500); catContainer.style.left = parentWin.evoriState.posX + "px"; catBody.style.transform = "rotate(1080deg) scale(1.5)";
                    let upTrail = setInterval(() => { const rect = catContainer.getBoundingClientRect(); const t = parentDoc.createElement('div'); t.className = 'cat-meteor-trail'; t.style.left = (rect.left + 35) + 'px'; t.style.top = (rect.top + 40) + 'px'; t.style.transform = parentWin.evoriState.facingRight ? 'rotate(45deg)' : 'rotate(-45deg)'; parentDoc.body.appendChild(t); setTimeout(() => t.remove(), 1000); }, 30);
                    setTimeout(() => {
                        clearInterval(upTrail); catContainer.style.transition = "none"; catContainer.style.bottom = "110vh";
                        parentWin.evoriState.posX = parentDoc.documentElement.clientWidth / 2; catContainer.style.left = parentWin.evoriState.posX + "px"; catBody.style.transform = "rotate(180deg) scale(2)"; 
                        setTimeout(() => {
                            catContainer.style.transition = "bottom 0.4s cubic-bezier(0.8, 0, 1, 1)"; catContainer.style.bottom = "20px";
                            let downTrail = setInterval(() => { const rect = catContainer.getBoundingClientRect(); const t = parentDoc.createElement('div'); t.className = 'cat-meteor-trail'; t.style.left = (rect.left + 35) + 'px'; t.style.top = (rect.top - 20) + 'px'; t.style.transform = 'rotate(180deg)'; parentDoc.body.appendChild(t); setTimeout(() => t.remove(), 1000); }, 25);
                            setTimeout(() => { clearInterval(downTrail); catBody.style.transform = parentWin.evoriState.facingRight ? 'scaleX(1)' : 'scaleX(-1)'; for(let i=0; i<15; i++) parentWin.evoriActions.createParticle('💥'); parentWin.evoriActions.speak(null, "Nailed it. 😵‍💫"); setTimeout(() => { catContainer.style.transition = "bottom 0.3s cubic-bezier(0.25, 0.8, 0.25, 1)"; }, 1000); }, 400); 
                        }, 50);
                    }, 600);
                }
            };

            // ==========================================
            // 🧠 PROGRAMMABLE PERSONALITY ENGINE
            // You can easily change what she says here!
            // ==========================================
           function getKittyResponse(msg) {
                let lowerMsg = msg.toLowerCase();
                
                // 1. SMART LIBRARY FLEXIBLE SEARCH
                if(lowerMsg.includes("search") || lowerMsg.includes("find") || lowerMsg.includes("look") || lowerMsg.includes("document") || lowerMsg.includes("library") || lowerMsg.includes("want") || lowerMsg.includes("need")) {
                    if(libraryFiles.length === 0) return "My library is empty! Upload a .zip file in the sidebar first! 🐾";
                    
                    let cleanMsg = lowerMsg.replace(/[?.,!]/g, '');
                    
                    // A massive list of conversational words for Evori to ignore
                    const stopWords = ["i", "want", "need", "give", "show", "me", "a", "an", "the", "some", "any", "all", "list", "of", "search", "find", "look", "up", "for", "document", "documents", "file", "files", "in", "library", "about", "topic", "containing", "contain", "can", "you", "please", "evori", "get"];
                    
                    let words = cleanMsg.split(' ').filter(w => !stopWords.includes(w) && w.trim() !== "");
                    
                    if(words.length === 0) return "What specific topic or filename should I sniff out? 🐾";
                    
                    // Flexible Search: If ANY of the core keywords match the filename, it's a hit!
                    let found = libraryFiles.filter(f => {
                        let safeFileName = f.toLowerCase().replace(/[_-]/g, ' ');
                        return words.some(w => safeFileName.includes(w));
                    });
                    
                    if(found.length > 0) {
                        let listHTML = found.slice(0, 5).map(f => {
                            let safeName = encodeURIComponent(f);
                            let dispName = f.replace(/</g, "&lt;").replace(/>/g, "&gt;");
                            return "<br>📄 <a href='?doc=" + safeName + "' target='_parent' onclick='window.parent.sessionStorage.setItem(\\"evoriChat\\", window.parent.document.getElementById(\\"chat-content\\").innerHTML); window.parent.sessionStorage.setItem(\\"evoriPosX\\", window.parent.evoriState.posX); window.parent.sessionStorage.setItem(\\"evoriFacing\\", window.parent.evoriState.facingRight);' style='color:var(--evori-pri); text-decoration:underline; font-weight:bold; cursor:pointer;'>" + dispName + "</a>";
                        }).join("");
                        
                        let responseText = "Meow! 📚 I sniffed through the library and found:" + listHTML;
                        if(found.length > 5) responseText += "<br><i>...and " + (found.length - 5) + " more!</i>";
                        return responseText;
                    } else {
                        return "I dug through the files but didn't find anything matching '" + words.join(" ") + "'. 😿";
                    }
                }
                
                // 2. RULES ENGINE (Triggers -> Response)
                const rules = [
                    { triggers: ["hello", "hi", "hey", "greetings"], response: "Meow! Welcome back to the dashboard! ✨🐾" },
                    { triggers: ["how are you", "doing", "what's up"], response: "*purrrr* I'm doing great! Just keeping an eye on your data! 🐱💖" },
                    { triggers: ["kamikaze", "attack", "fly"], response: "Did someone say KAMIKAZE?! 🚀💥" },
                    { triggers: ["love you", "cute", "adorable"], response: "Aww, *happy purrs* You're the best! 💖✨" },
                    { triggers: ["money", "finance", "budget"], response: "I only accept payment in catnip and tuna! 🐟💰" },
                    { triggers: ["strategy", "plan", "smart"], response: "My strategy is to nap 18 hours a day. Highly effective! 🧐💤" },
                    { triggers: ["who are you", "name"], response: "I am Evori Dreamwings! Your magical AI familiar! ✨" },
                    { triggers: ["tired", "stressed", "hard", "giving up"], response: "Take a deep breath! You are brilliant, and you've totally got this! 💖✨" },
                    { triggers: ["procrastinating", "lazy", "distracted"], response: "Focus! 😾 We have an empire to build! Get back to the dashboard!" }
                ];

                for (let rule of rules) {
                    if (rule.triggers.some(trigger => lowerMsg.includes(trigger))) {
                        return rule.response;
                    }
                }

                // 3. MAGIC 8-BALL LOGIC
                if(lowerMsg.endsWith("?")) { 
                    const answers = ["Hmm... meow! The data says Yes! ✨", "No way! 😾", "Let me consult the stars... ✨ yes!", "I wouldn't bet my tuna on it. 🐟"]; 
                    return answers[Math.floor(Math.random() * answers.length)]; 
                }
                
                // 4. FALLBACK RANDOM RESPONSES
                const randoms = ["Meow! 🐾", "*purrrrrr* 💖", "I'm just a magical cat! ✨", "Feed me more data! 🐟📊", "Is it time for a nap yet? 💤", "Wow, look at all these charts! 📈"];
                return randoms[Math.floor(Math.random() * randoms.length)];
            }
                
                // 2. RULES ENGINE (Triggers -> Response)
                // Add your own custom triggers and rules below!
                const rules = [
                    { triggers: ["hello", "hi", "hey", "greetings"], response: "Meow! Welcome back to the dashboard! ✨🐾" },
                    { triggers: ["how are you", "doing", "what's up"], response: "*purrrr* I'm doing great! Just keeping an eye on your data! 🐱💖" },
                    { triggers: ["kamikaze", "attack", "fly"], response: "Did someone say KAMIKAZE?! 🚀💥" },
                    { triggers: ["love you", "cute", "adorable"], response: "Aww, *happy purrs* You're the best! 💖✨" },
                    { triggers: ["money", "finance", "budget"], response: "I only accept payment in catnip and tuna! 🐟💰" },
                    { triggers: ["strategy", "plan", "smart"], response: "My strategy is to nap 18 hours a day. Highly effective! 🧐💤" },
                    { triggers: ["who are you", "name"], response: "I am Evori Dreamwings! Your magical AI familiar! ✨" },
                ];

                for (let rule of rules) {
                    if (rule.triggers.some(trigger => lowerMsg.includes(trigger))) {
                        return rule.response;
                    }
                }

                // 3. MAGIC 8-BALL LOGIC (If it ends in a Question Mark)
                if(lowerMsg.endsWith("?")) { 
                    const answers = ["Hmm... meow! The data says Yes! ✨", "No way! 😾", "Let me consult the stars... ✨ yes!", "I wouldn't bet my tuna on it. 🐟"]; 
                    return answers[Math.floor(Math.random() * answers.length)]; 
                }
                
                // 4. FALLBACK RANDOM RESPONSES
                const randoms = ["Meow! 🐾", "*purrrrrr* 💖", "I'm just a magical cat! ✨", "Feed me more data! 🐟📊", "Is it time for a nap yet? 💤", "Wow, look at all these charts! 📈"];
                return randoms[Math.floor(Math.random() * randoms.length)];
            }

            const chatContent = chatbox.querySelector('#chat-content');
            const chatInput = chatbox.querySelector('#chat-input');
            const chatSend = chatbox.querySelector('#chat-send');
            
            function sendToCat() {
                const text = chatInput.value.trim(); if (!text) return;
                const dUser = parentDoc.createElement('div'); dUser.className = 'msg-user'; dUser.innerText = text; chatContent.appendChild(dUser);
                chatInput.value = ''; chatContent.scrollTop = chatContent.scrollHeight;
                window.parent.sessionStorage.setItem('evoriChat', chatContent.innerHTML);

                setTimeout(() => {
                    const reply = getKittyResponse(text);
                    const dCat = parentDoc.createElement('div'); dCat.className = 'msg-cat'; dCat.innerHTML = reply; chatContent.appendChild(dCat);
                    chatContent.scrollTop = chatContent.scrollHeight;
                    
                    const textOnlyReply = reply.replace(/<[^>]*>?/gm, ''); 
                    parentWin.evoriActions.speak(null, textOnlyReply);
                    
                    catContainer.style.bottom = '80px'; setTimeout(() => { catContainer.style.bottom = '20px'; }, 300);
                    window.parent.sessionStorage.setItem('evoriChat', chatContent.innerHTML);
                }, 600);
            }

            chatSend.addEventListener('click', sendToCat);
            chatInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') sendToCat(); });

            catContainer.addEventListener('mouseover', () => { if (!parentWin.evoriState.isSleeping) { catBody.style.animation = 'float 0.5s infinite'; if (Math.random() > 0.8) parentWin.evoriActions.createParticle('✨'); } });
            catContainer.addEventListener('mouseout', () => { if (!parentWin.evoriState.isSleeping) catBody.style.animation = 'walk 1s infinite'; });
            catContainer.addEventListener('click', () => {
                if (Math.random() <= 0.30) { parentWin.evoriActions.triggerKamikaze(); } else {
                    parentWin.evoriState.isSleeping = false; catContainer.style.bottom = '80px';
                    setTimeout(() => { catContainer.style.bottom = '20px'; }, 300);
                    setTimeout(() => { if(Math.random() > 0.5) { catContainer.style.bottom = '80px'; setTimeout(() => { catContainer.style.bottom = '20px'; }, 300); } }, 350); 
                    parentWin.evoriActions.createParticle('💖'); parentWin.evoriActions.speak(null, "Meow! 🐾");
                }
            });

            parentWin.evoriLoop = setInterval(() => {
                const state = parentWin.evoriState;
                if (parentDoc.getElementById('evori-chatbox').matches(':hover') || parentDoc.getElementById('evori-chatbox').matches(':focus-within')) return; 
                if (Math.random() < 0.01 && !state.isSleeping && !catContainer.style.transition.includes("all")) {
                    state.isSleeping = true; catBody.style.animation = 'sleep 3s infinite'; parentWin.evoriActions.speak(null, "Zzz... 💤");
                    setTimeout(() => { state.isSleeping = false; catBody.style.animation = 'walk 1s infinite'; }, 5000);
                }
                if (!state.isSleeping && !state.isIdle && !catContainer.style.transition.includes("all")) {
                    state.posX += state.velocityX; catBody.style.animation = 'walk 1s infinite';
                    const maxRight = parentWin.innerWidth - 360;
                    if (state.posX > maxRight || state.posX < 10) {
                        state.isIdle = true; catBody.style.animation = 'float 2s infinite';
                        setTimeout(() => {
                            state.velocityX *= -1;
                            if (state.posX > maxRight) state.posX = maxRight - 10;
                            if (state.posX < 10) state.posX = 10;
                            state.facingRight = state.velocityX > 0;
                            catBody.style.transform = state.facingRight ? 'scaleX(1)' : 'scaleX(-1)';
                            const bubble = parentDoc.getElementById('cat-speech');
                            if(bubble) bubble.style.transform = state.facingRight ? 'translateX(-50%) scaleX(1)' : 'translateX(-50%) scaleX(-1)';
                            state.isIdle = false;
                        }, 2000); 
                    }
                    catContainer.style.left = state.posX + 'px';
                }
            }, 30);
            
            const passedMode = "{CAT_MODE}";
            const catContainerRef = parentDoc.getElementById('evori-cat-companion');
            if (catContainerRef && catContainerRef.dataset.mode !== passedMode) {
                catContainerRef.dataset.mode = passedMode;
                if(typeof updateAccessory === 'function') updateAccessory(passedMode);
            }
        </script>
        """.replace("{C_PRI}", c_pri).replace("{C_SEC}", c_sec).replace("{C_GLOW}", c_glow).replace("{BG_SIDE}", bg_side).replace("{CAT_HUE}", cat_hue).replace("{FILES_JSON}", files_json)
        components.html(EVORI_HTML, height=0, width=0)
    else:
        components.html("""
        <script>
            if(window.parent.evoriLoop) clearInterval(window.parent.evoriLoop);
            const c = window.parent.document.getElementById('evori-cat-companion');
            const box = window.parent.document.getElementById('evori-chatbox');
            if(c) c.remove(); if(box) box.remove();
        </script>
        """, height=0, width=0)
