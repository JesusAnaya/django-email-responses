
var MediaFileBrowser = function(field_name, url, type, win)
{
    var cmsURL = '/admin/media-library/browse/?pop=2';
    cmsURL += '&type=' + type;

    tinymce.activeEditor.windowManager.open({
        title: "File browser",
        file: cmsURL,
        width: 980,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'no',  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: 'no'
    }, {
        setUrl: function (url) {
            win.document.getElementById(field_name).value = url;
        },
        window: win,
        input: field_name
    });
    return false;
};

tinymce.init({
    selector: ".mceEditor",
    width: 800,
    height: 500,
    file_browser_callback: MediaFileBrowser,
    relative_urls: false,

    plugins: [
        "compat3x advlist autolink lists link image charmap print preview anchor",
        "searchreplace visualblocks code fullscreen",
        "insertdatetime media table contextmenu paste"
    ],

    toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
    autosave_ask_before_unload: false,
});
