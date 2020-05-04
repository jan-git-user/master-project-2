(function() {
    var el = document.createElement('script');
    el.src = 'https://code.jquery.com/jquery-3.3.1.min.js';
    el.async = true;
    el.addEventListener('load', function() { window.google_tag_manager[{{Container ID}}].onHtmlSuccess({{HTML ID}})});
    el.addEventListener('error', function() { window.google_tag_manager[{{Container ID}}].onHtmlFailure({{HTML ID}})});
    document.head.appendChild(el);
  })();