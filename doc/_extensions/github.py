  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>ipython/docs/sphinxext/github.py at master · ipython/ipython · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <link rel="xhr-socket" href="/_sockets" />


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="KxkHbu6uuzb5nYpICaiM/tuRIpoRIcTZQEgfU8NliZg=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-d63f89e307e2e357d3b7160b3cd4020463f9bbc1.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-4a2696ec075bd8d27843df00793c7e9d6525dded.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-92d138f450f2960501e28397a2f63b0f100590f0.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-60bb3beedc339be272bd2acfce1cae3b79371737.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="7159fafc2fc92e02281814323bde3687">

        <link data-pjax-transient rel='permalink' href='/ipython/ipython/blob/831d4eb049fa74f8be85ea7495a9724cb754390f/docs/sphinxext/github.py'>
    <meta property="og:title" content="ipython"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/ipython/ipython"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/f72497397dd9a0a79c654c8182460bb1?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="ipython - Official repository for IPython itself. Other repos in the IPython organization contain things like the website, documentation builds, etc."/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="ipython/ipython"/>

    <meta name="description" content="ipython - Official repository for IPython itself. Other repos in the IPython organization contain things like the website, documentation builds, etc." />


    <meta content="230453" name="octolytics-dimension-user_id" /><meta content="658518" name="octolytics-dimension-repository_id" />
  <link href="https://github.com/ipython/ipython/commits/master.atom" rel="alternate" title="Recent Commits to ipython:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob windows vis-public env-production  ">
    <div id="wrapper">

      

      
      
      

      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">Github</a>

    <div class="header-actions">
      <a class="button primary" href="https://github.com/signup">Sign up</a>
      <a class="button" href="https://github.com/login?return_to=%2Fipython%2Fipython%2Fblob%2Fmaster%2Fdocs%2Fsphinxext%2Fgithub.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">


      <ul class="top-nav">
          <li class="explore"><a href="https://github.com/explore">Explore</a></li>
        <li class="features"><a href="https://github.com/features">Features</a></li>
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">
  <a href="/search/advanced" class="advanced-search-icon tooltipped downwards command-bar-search" id="advanced_search" title="Advanced search"><span class="octicon octicon-gear "></span></a>

  <input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
      data-repo="ipython/ipython"
      data-branch="master"
      data-sha="26bb5f152ca86cb76eb66799c54e217638cd4b6d"
  >

    <input type="hidden" name="nwo" value="ipython/ipython" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

  <div class="divider-vertical"></div>

</form>
    </div>

  </div>
</div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2Fipython%2Fipython"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="octicon octicon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/ipython/ipython/stargazers">
        1,895
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fipython%2Fipython"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/ipython/ipython/network" class="social-count">
        586
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-octicon octicon-repo"></span>
                <span class="author vcard">
                  <a href="/ipython" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">ipython</span>
                  </a></span> /
                <strong><a href="/ipython/ipython" class="js-current-repository">ipython</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/ipython/ipython/pulse" class="js-selected-navigation-item " data-selected-links="pulse /ipython/ipython/pulse" rel="nofollow"><span class="octicon octicon-pulse"></span></a></li>
    <li><a href="/ipython/ipython" class="js-selected-navigation-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /ipython/ipython">Code</a></li>
    <li><a href="/ipython/ipython/network" class="js-selected-navigation-item " data-selected-links="repo_network /ipython/ipython/network">Network</a></li>
    <li><a href="/ipython/ipython/pulls" class="js-selected-navigation-item " data-selected-links="repo_pulls /ipython/ipython/pulls">Pull Requests <span class='counter'>15</span></a></li>

      <li><a href="/ipython/ipython/issues" class="js-selected-navigation-item " data-selected-links="repo_issues /ipython/ipython/issues">Issues <span class='counter'>567</span></a></li>

      <li><a href="/ipython/ipython/wiki" class="js-selected-navigation-item " data-selected-links="repo_wiki /ipython/ipython/wiki">Wiki</a></li>


    <li><a href="/ipython/ipython/graphs" class="js-selected-navigation-item " data-selected-links="repo_graphs repo_contributors /ipython/ipython/graphs">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/ipython/ipython/tags" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_tags /ipython/ipython/tags">Tags <span class="counter ">13</span></a></li>
    </ul>
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="octicon octicon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/0.10.2/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.10.2" rel="nofollow" title="0.10.2">0.10.2</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/0.12.1/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.12.1" rel="nofollow" title="0.12.1">0.12.1</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/0.13.x/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="0.13.x" rel="nofollow" title="0.13.x">0.13.x</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/master/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.13.2/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.13.2" rel="nofollow" title="rel-0.13.2">rel-0.13.2</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.13.1/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.13.1" rel="nofollow" title="rel-0.13.1">rel-0.13.1</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.13/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.13" rel="nofollow" title="rel-0.13">rel-0.13</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.12.1/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.12.1" rel="nofollow" title="rel-0.12.1">rel-0.12.1</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.12/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.12" rel="nofollow" title="rel-0.12">rel-0.12</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.11/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.11" rel="nofollow" title="rel-0.11">rel-0.11</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.10.2/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.10.2" rel="nofollow" title="rel-0.10.2">rel-0.10.2</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.10.1/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.10.1" rel="nofollow" title="rel-0.10.1">rel-0.10.1</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.10/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.10" rel="nofollow" title="rel-0.10">rel-0.10</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.9.1/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.9.1" rel="nofollow" title="rel-0.9.1">rel-0.9.1</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.9/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.9" rel="nofollow" title="rel-0.9">rel-0.9</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/rel-0.8.4/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="rel-0.8.4" rel="nofollow" title="rel-0.8.4">rel-0.8.4</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/ipython/ipython/blob/dev-0.11/docs/sphinxext/github.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="dev-0.11" rel="nofollow" title="dev-0.11">dev-0.11</a>
                </div> <!-- /.select-menu-item -->
            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/ipython/ipython" class="selected js-selected-navigation-item tabnav-tab" data-selected-links="repo_source /ipython/ipython">Files</a></li>
    <li><a href="/ipython/ipython/commits/master" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_commits /ipython/ipython/commits/master">Commits</a></li>
    <li><a href="/ipython/ipython/branches" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_branches /ipython/ipython/branches" rel="nofollow">Branches <span class="counter ">4</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:5a715cc18d66347c4a5af2652afee082 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:5a715cc18d66347c4a5af2652afee082 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ipython/ipython" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">ipython</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ipython/ipython/tree/master/docs" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">docs</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ipython/ipython/tree/master/docs/sphinxext" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">sphinxext</span></a></span><span class="separator"> / </span><strong class="final-path">github.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="docs/sphinxext/github.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
        </div>

      <a href="/ipython/ipython/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/ipython/ipython/contributors/master/docs/sphinxext/github.py">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif?1340659530" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>

    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/ipython/ipython/blob/831d4eb049fa74f8be85ea7495a9724cb754390f/docs/sphinxext/github.py" data-title="ipython/docs/sphinxext/github.py at master · ipython/ipython · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>156 lines (132 sloc)</span>
                <span>5.379 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/ipython/ipython/raw/master/docs/sphinxext/github.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/ipython/ipython/blame/master/docs/sphinxext/github.py" class="button minibutton ">Blame</a>
                  <a href="/ipython/ipython/commits/master/docs/sphinxext/github.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="sd">&quot;&quot;&quot;Define text roles for GitHub</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="sd">* ghissue - Issue</span></div><div class='line' id='LC4'><span class="sd">* ghpull - Pull Request</span></div><div class='line' id='LC5'><span class="sd">* ghuser - User</span></div><div class='line' id='LC6'><br/></div><div class='line' id='LC7'><span class="sd">Adapted from bitbucket example here:</span></div><div class='line' id='LC8'><span class="sd">https://bitbucket.org/birkenfeld/sphinx-contrib/src/tip/bitbucket/sphinxcontrib/bitbucket.py</span></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><span class="sd">Authors</span></div><div class='line' id='LC11'><span class="sd">-------</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="sd">* Doug Hellmann</span></div><div class='line' id='LC14'><span class="sd">* Min RK</span></div><div class='line' id='LC15'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC16'><span class="c">#</span></div><div class='line' id='LC17'><span class="c"># Original Copyright (c) 2010 Doug Hellmann.  All rights reserved.</span></div><div class='line' id='LC18'><span class="c">#</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="kn">from</span> <span class="nn">docutils</span> <span class="kn">import</span> <span class="n">nodes</span><span class="p">,</span> <span class="n">utils</span></div><div class='line' id='LC21'><span class="kn">from</span> <span class="nn">docutils.parsers.rst.roles</span> <span class="kn">import</span> <span class="n">set_classes</span></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'><span class="k">def</span> <span class="nf">make_link_node</span><span class="p">(</span><span class="n">rawtext</span><span class="p">,</span> <span class="n">app</span><span class="p">,</span> <span class="nb">type</span><span class="p">,</span> <span class="n">slug</span><span class="p">,</span> <span class="n">options</span><span class="p">):</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Create a link to a github resource.</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'><span class="sd">    :param rawtext: Text being replaced with link node.</span></div><div class='line' id='LC27'><span class="sd">    :param app: Sphinx application context</span></div><div class='line' id='LC28'><span class="sd">    :param type: Link type (issues, changeset, etc.)</span></div><div class='line' id='LC29'><span class="sd">    :param slug: ID of the thing to link to</span></div><div class='line' id='LC30'><span class="sd">    :param options: Options dictionary passed to role func.</span></div><div class='line' id='LC31'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">base</span> <span class="o">=</span> <span class="n">app</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">github_project_url</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">base</span><span class="p">:</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">AttributeError</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">base</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">):</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">base</span> <span class="o">+=</span> <span class="s">&#39;/&#39;</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">AttributeError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;github_project_url configuration value is not set (</span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="nb">str</span><span class="p">(</span><span class="n">err</span><span class="p">))</span></div><div class='line' id='LC41'><br/></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ref</span> <span class="o">=</span> <span class="n">base</span> <span class="o">+</span> <span class="nb">type</span> <span class="o">+</span> <span class="s">&#39;/&#39;</span> <span class="o">+</span> <span class="n">slug</span> <span class="o">+</span> <span class="s">&#39;/&#39;</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">set_classes</span><span class="p">(</span><span class="n">options</span><span class="p">)</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span> <span class="o">=</span> <span class="s">&quot;#&quot;</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">type</span> <span class="o">==</span> <span class="s">&#39;pull&#39;</span><span class="p">:</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prefix</span> <span class="o">=</span> <span class="s">&quot;PR &quot;</span> <span class="o">+</span> <span class="n">prefix</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">node</span> <span class="o">=</span> <span class="n">nodes</span><span class="o">.</span><span class="n">reference</span><span class="p">(</span><span class="n">rawtext</span><span class="p">,</span> <span class="n">prefix</span> <span class="o">+</span> <span class="n">utils</span><span class="o">.</span><span class="n">unescape</span><span class="p">(</span><span class="n">slug</span><span class="p">),</span> <span class="n">refuri</span><span class="o">=</span><span class="n">ref</span><span class="p">,</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">**</span><span class="n">options</span><span class="p">)</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">node</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'><span class="k">def</span> <span class="nf">ghissue_role</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">rawtext</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">lineno</span><span class="p">,</span> <span class="n">inliner</span><span class="p">,</span> <span class="n">options</span><span class="o">=</span><span class="p">{},</span> <span class="n">content</span><span class="o">=</span><span class="p">[]):</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Link to a GitHub issue.</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'><span class="sd">    Returns 2 part tuple containing list of nodes to insert into the</span></div><div class='line' id='LC55'><span class="sd">    document and a list of system messages.  Both are allowed to be</span></div><div class='line' id='LC56'><span class="sd">    empty.</span></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><span class="sd">    :param name: The role name used in the document.</span></div><div class='line' id='LC59'><span class="sd">    :param rawtext: The entire markup snippet, with role.</span></div><div class='line' id='LC60'><span class="sd">    :param text: The text marked with the role.</span></div><div class='line' id='LC61'><span class="sd">    :param lineno: The line number where rawtext appears in the input.</span></div><div class='line' id='LC62'><span class="sd">    :param inliner: The inliner instance that called us.</span></div><div class='line' id='LC63'><span class="sd">    :param options: Directive options for customization.</span></div><div class='line' id='LC64'><span class="sd">    :param content: The directive content for customization.</span></div><div class='line' id='LC65'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC66'><br/></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">issue_num</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">text</span><span class="p">)</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">issue_num</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">ValueError</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msg</span> <span class="o">=</span> <span class="n">inliner</span><span class="o">.</span><span class="n">reporter</span><span class="o">.</span><span class="n">error</span><span class="p">(</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;GitHub issue number must be a number greater than or equal to 1; &#39;</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;&quot;</span><span class="si">%s</span><span class="s">&quot; is invalid.&#39;</span> <span class="o">%</span> <span class="n">text</span><span class="p">,</span> <span class="n">line</span><span class="o">=</span><span class="n">lineno</span><span class="p">)</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prb</span> <span class="o">=</span> <span class="n">inliner</span><span class="o">.</span><span class="n">problematic</span><span class="p">(</span><span class="n">rawtext</span><span class="p">,</span> <span class="n">rawtext</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">prb</span><span class="p">],</span> <span class="p">[</span><span class="n">msg</span><span class="p">]</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span> <span class="o">=</span> <span class="n">inliner</span><span class="o">.</span><span class="n">document</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">env</span><span class="o">.</span><span class="n">app</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#app.info(&#39;issue %r&#39; % text)</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;pull&#39;</span> <span class="ow">in</span> <span class="n">name</span><span class="o">.</span><span class="n">lower</span><span class="p">():</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">category</span> <span class="o">=</span> <span class="s">&#39;pull&#39;</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="s">&#39;issue&#39;</span> <span class="ow">in</span> <span class="n">name</span><span class="o">.</span><span class="n">lower</span><span class="p">():</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">category</span> <span class="o">=</span> <span class="s">&#39;issues&#39;</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msg</span> <span class="o">=</span> <span class="n">inliner</span><span class="o">.</span><span class="n">reporter</span><span class="o">.</span><span class="n">error</span><span class="p">(</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;GitHub roles include &quot;ghpull&quot; and &quot;ghissue&quot;, &#39;</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;&quot;</span><span class="si">%s</span><span class="s">&quot; is invalid.&#39;</span> <span class="o">%</span> <span class="n">name</span><span class="p">,</span> <span class="n">line</span><span class="o">=</span><span class="n">lineno</span><span class="p">)</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prb</span> <span class="o">=</span> <span class="n">inliner</span><span class="o">.</span><span class="n">problematic</span><span class="p">(</span><span class="n">rawtext</span><span class="p">,</span> <span class="n">rawtext</span><span class="p">,</span> <span class="n">msg</span><span class="p">)</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">prb</span><span class="p">],</span> <span class="p">[</span><span class="n">msg</span><span class="p">]</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">node</span> <span class="o">=</span> <span class="n">make_link_node</span><span class="p">(</span><span class="n">rawtext</span><span class="p">,</span> <span class="n">app</span><span class="p">,</span> <span class="n">category</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">issue_num</span><span class="p">),</span> <span class="n">options</span><span class="p">)</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="p">],</span> <span class="p">[]</span></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'><span class="k">def</span> <span class="nf">ghuser_role</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">rawtext</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">lineno</span><span class="p">,</span> <span class="n">inliner</span><span class="p">,</span> <span class="n">options</span><span class="o">=</span><span class="p">{},</span> <span class="n">content</span><span class="o">=</span><span class="p">[]):</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Link to a GitHub user.</span></div><div class='line' id='LC94'><br/></div><div class='line' id='LC95'><span class="sd">    Returns 2 part tuple containing list of nodes to insert into the</span></div><div class='line' id='LC96'><span class="sd">    document and a list of system messages.  Both are allowed to be</span></div><div class='line' id='LC97'><span class="sd">    empty.</span></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'><span class="sd">    :param name: The role name used in the document.</span></div><div class='line' id='LC100'><span class="sd">    :param rawtext: The entire markup snippet, with role.</span></div><div class='line' id='LC101'><span class="sd">    :param text: The text marked with the role.</span></div><div class='line' id='LC102'><span class="sd">    :param lineno: The line number where rawtext appears in the input.</span></div><div class='line' id='LC103'><span class="sd">    :param inliner: The inliner instance that called us.</span></div><div class='line' id='LC104'><span class="sd">    :param options: Directive options for customization.</span></div><div class='line' id='LC105'><span class="sd">    :param content: The directive content for customization.</span></div><div class='line' id='LC106'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span> <span class="o">=</span> <span class="n">inliner</span><span class="o">.</span><span class="n">document</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">env</span><span class="o">.</span><span class="n">app</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#app.info(&#39;user link %r&#39; % text)</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ref</span> <span class="o">=</span> <span class="s">&#39;https://www.github.com/&#39;</span> <span class="o">+</span> <span class="n">text</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">node</span> <span class="o">=</span> <span class="n">nodes</span><span class="o">.</span><span class="n">reference</span><span class="p">(</span><span class="n">rawtext</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">refuri</span><span class="o">=</span><span class="n">ref</span><span class="p">,</span> <span class="o">**</span><span class="n">options</span><span class="p">)</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="p">],</span> <span class="p">[]</span></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'><span class="k">def</span> <span class="nf">ghcommit_role</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">rawtext</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">lineno</span><span class="p">,</span> <span class="n">inliner</span><span class="p">,</span> <span class="n">options</span><span class="o">=</span><span class="p">{},</span> <span class="n">content</span><span class="o">=</span><span class="p">[]):</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Link to a GitHub commit.</span></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'><span class="sd">    Returns 2 part tuple containing list of nodes to insert into the</span></div><div class='line' id='LC117'><span class="sd">    document and a list of system messages.  Both are allowed to be</span></div><div class='line' id='LC118'><span class="sd">    empty.</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'><span class="sd">    :param name: The role name used in the document.</span></div><div class='line' id='LC121'><span class="sd">    :param rawtext: The entire markup snippet, with role.</span></div><div class='line' id='LC122'><span class="sd">    :param text: The text marked with the role.</span></div><div class='line' id='LC123'><span class="sd">    :param lineno: The line number where rawtext appears in the input.</span></div><div class='line' id='LC124'><span class="sd">    :param inliner: The inliner instance that called us.</span></div><div class='line' id='LC125'><span class="sd">    :param options: Directive options for customization.</span></div><div class='line' id='LC126'><span class="sd">    :param content: The directive content for customization.</span></div><div class='line' id='LC127'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span> <span class="o">=</span> <span class="n">inliner</span><span class="o">.</span><span class="n">document</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">env</span><span class="o">.</span><span class="n">app</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#app.info(&#39;user link %r&#39; % text)</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">base</span> <span class="o">=</span> <span class="n">app</span><span class="o">.</span><span class="n">config</span><span class="o">.</span><span class="n">github_project_url</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">base</span><span class="p">:</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">AttributeError</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">base</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">):</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">base</span> <span class="o">+=</span> <span class="s">&#39;/&#39;</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">AttributeError</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;github_project_url configuration value is not set (</span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="nb">str</span><span class="p">(</span><span class="n">err</span><span class="p">))</span></div><div class='line' id='LC138'><br/></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ref</span> <span class="o">=</span> <span class="n">base</span> <span class="o">+</span> <span class="n">text</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">node</span> <span class="o">=</span> <span class="n">nodes</span><span class="o">.</span><span class="n">reference</span><span class="p">(</span><span class="n">rawtext</span><span class="p">,</span> <span class="n">text</span><span class="p">[:</span><span class="mi">6</span><span class="p">],</span> <span class="n">refuri</span><span class="o">=</span><span class="n">ref</span><span class="p">,</span> <span class="o">**</span><span class="n">options</span><span class="p">)</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">node</span><span class="p">],</span> <span class="p">[]</span></div><div class='line' id='LC142'><br/></div><div class='line' id='LC143'><br/></div><div class='line' id='LC144'><span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="n">app</span><span class="p">):</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Install the plugin.</span></div><div class='line' id='LC146'><span class="sd">    </span></div><div class='line' id='LC147'><span class="sd">    :param app: Sphinx application context.</span></div><div class='line' id='LC148'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Initializing GitHub plugin&#39;</span><span class="p">)</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span><span class="o">.</span><span class="n">add_role</span><span class="p">(</span><span class="s">&#39;ghissue&#39;</span><span class="p">,</span> <span class="n">ghissue_role</span><span class="p">)</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span><span class="o">.</span><span class="n">add_role</span><span class="p">(</span><span class="s">&#39;ghpull&#39;</span><span class="p">,</span> <span class="n">ghissue_role</span><span class="p">)</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span><span class="o">.</span><span class="n">add_role</span><span class="p">(</span><span class="s">&#39;ghuser&#39;</span><span class="p">,</span> <span class="n">ghuser_role</span><span class="p">)</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span><span class="o">.</span><span class="n">add_role</span><span class="p">(</span><span class="s">&#39;ghcommit&#39;</span><span class="p">,</span> <span class="n">ghcommit_role</span><span class="p">)</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">app</span><span class="o">.</span><span class="n">add_config_value</span><span class="p">(</span><span class="s">&#39;github_project_url&#39;</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="s">&#39;env&#39;</span><span class="p">)</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1347543525" height="64" width="64">
</div>


        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.12974s from fe17.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/ipython/ipython/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="octicon octicon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.13024' data-host='fe17'></span>
    
  </body>
</html>

