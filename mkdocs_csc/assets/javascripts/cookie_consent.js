window.cookieconsent.initialise({
    "palette": {
        "popup": {
            "background": "#237afc"
        },
        "button": {
            "background": "#fff",
            "text": "#237afc"
        }
    },
    onStatusChange: function(status) {
        if(this.hasConsented()){
            cookieconsent.status = "allow";
            window[`ga-disable-${window._csc_ga_id}`] = false
            location.reload(); 
        }
        else{
            cookieconsent.status = "deny";
            window[`ga-disable-${window._csc_ga_id}`] = true
            document.cookie = `_gat= ; expires= Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain= ${window.location.hostname};`;
            document.cookie = `_ga= ; expires= Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain= ${window.location.hostname};`;
            document.cookie = `_gid= ; expires= Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain= ${window.location.hostname};`;
            location.reload(); 

        }
    },

    "type": "opt-in"
});
