
  
  

  


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html;charset=UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <title>dataTools/importMatlabData.py at master from faridani's PyNLP - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="http://github.com/fluidicon.png" title="GitHub" />

    <link href="http://assets3.github.com/stylesheets/bundle_common.css?ff378e631d68c65b4c5c52a30c91c5851c1c721b" media="screen" rel="stylesheet" type="text/css" />
<link href="http://assets2.github.com/stylesheets/bundle_github.css?ff378e631d68c65b4c5c52a30c91c5851c1c721b" media="screen" rel="stylesheet" type="text/css" />

    <script type="text/javascript" charset="utf-8">
      var GitHub = {}
      var github_user = 'faridani'
      
    </script>
    <script src="http://assets1.github.com/javascripts/jquery/jquery-1.4.2.min.js?ff378e631d68c65b4c5c52a30c91c5851c1c721b" type="text/javascript"></script>
    <script src="http://assets1.github.com/javascripts/bundle_common.js?ff378e631d68c65b4c5c52a30c91c5851c1c721b" type="text/javascript"></script>
<script src="http://assets2.github.com/javascripts/bundle_github.js?ff378e631d68c65b4c5c52a30c91c5851c1c721b" type="text/javascript"></script>

        <script type="text/javascript" charset="utf-8">
      GitHub.spy({
        repo: "faridani/PyNLP"
      })
    </script>

    
  
    
  

  <link href="http://github.com/faridani/PyNLP/commits/master.atom" rel="alternate" title="Recent Commits to PyNLP:master" type="application/atom+xml" />

        <meta name="description" content="... just because nltk is too heavy" />
    <script type="text/javascript">
      GitHub.nameWithOwner = GitHub.nameWithOwner || "faridani/PyNLP";
      GitHub.currentRef = 'master';
    </script>
  

            <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-3769691-2']);
      _gaq.push(['_trackPageview']);
      (function() {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
      })();
    </script>

  </head>

  

  <body>
    

    
      <script type="text/javascript">
        var _kmq = _kmq || [];
        function _kms(u){
          var s = document.createElement('script'); var f = document.getElementsByTagName('script')[0]; s.type = 'text/javascript'; s.async = true;
          s.src = u; f.parentNode.insertBefore(s, f);
        }
        _kms('//i.kissmetrics.com/i.js');_kms('//doug1izaerwt3.cloudfront.net/406e8bf3a2b8846ead55afb3cfaf6664523e3a54.1.js');
      </script>
    

    

    

    

    <div class="subnavd" id="main">
      <div id="header" class="pageheaded">
        <div class="site">
          <div class="logo">
            <a href="https://github.com/"><img src="/images/modules/header/logov3.png" alt="github" /></a>
          </div>
          
            






  
    <div class="userbox">
      <div class="inner">
        <div class="avatarname">
          <a href="http://github.com/faridani"><img src="http://www.gravatar.com/avatar/46c83b6cafe5077dfdc0cd6b818e7e4f?s=140&d=http%3A%2F%2Fgithub.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="20" height="20"  /></a>
          <a href="http://github.com/faridani" class="name">faridani</a>

          
          
        </div>
        <ul class="usernav">
          <li><a href="https://github.com/">Dashboard</a></li>
          <li>
            
            <a href="https://github.com/inbox">Inbox</a>
            <a href="https://github.com/inbox" class="unread_count ">0</a>
          </li>
          <li><a href="https://github.com/account">Account Settings</a></li>
                              <li><a href="/logout">Log Out</a></li>
        </ul>
      </div>
    </div><!-- /.userbox -->
  


          
          <div class="topsearch">
  
    <form action="/search" id="top_search_form" method="get">
      <a href="/search" class="advanced-search tooltipped downwards" title="Advanced Search">Advanced Search</a>
      <input type="search" class="search my_repos_autocompleter" name="q" results="5" placeholder="Search&hellip;" /> <input type="submit" value="Search" class="button" />
      <input type="hidden" name="type" value="Everything" />
      <input type="hidden" name="repo" value="" />
      <input type="hidden" name="langOverride" value="" />
      <input type="hidden" name="start_value" value="1" />
    </form>
  
  
    <ul class="nav">
      <li><a href="/explore">Explore GitHub</a></li>
      <li><a href="http://gist.github.com">Gist</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="http://help.github.com">Help</a></li>
    </ul>
  
</div>

        </div>
      </div>

      
      
        
    <div class="site">
      <div class="pagehead repohead vis-public   ">
        <h1>
          <a href="/faridani">faridani</a> / <strong><a href="http://github.com/faridani/PyNLP">PyNLP</a></strong>
          
          
        </h1>

        
    <ul class="actions">
      

      
        <li class="for-owner" style="display:none"><a href="https://github.com/faridani/PyNLP/edit" class="minibutton btn-admin "><span><span class="icon"></span>Admin</span></a></li>
        <li>
          <a href="/faridani/PyNLP/toggle_watch" class="minibutton btn-watch " id="watch_button" style="display:none"><span><span class="icon"></span>Watch</span></a>
          <a href="/faridani/PyNLP/toggle_watch" class="minibutton btn-watch " id="unwatch_button" style="display:none"><span><span class="icon"></span>Unwatch</span></a>
        </li>
        
          
            <li class="for-notforked" style="display:none"><a href="/faridani/PyNLP/fork" class="minibutton btn-fork " id="fork_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '51a195d98d6f22525f998d49b2a520e9e3d83c74'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Fork</span></a></li>
            <li class="for-hasfork" style="display:none"><a href="#" class="minibutton btn-fork " id="your_fork_button"><span><span class="icon"></span>Your Fork</span></a></li>
          

          
          <li id="pull_request_item" class='ospr' style="display:none"><a href="/faridani/PyNLP/pull_request/" class="minibutton btn-pull-request "><span><span class="icon"></span>Pull Request</span></a></li>
          

          <li><a href="#" class="minibutton btn-download " id="download_button"><span><span class="icon"></span>Download Source</span></a></li>
        
      
      
      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers"><a href="/faridani/PyNLP/watchers" title="Watchers" class="tooltipped downwards">4</a></li>
          <li class="forks"><a href="/faridani/PyNLP/network" title="Forks" class="tooltipped downwards">1</a></li>
        </ul>
      </li>
    </ul>


        
  <ul class="tabs">
    <li><a href="http://github.com/faridani/PyNLP/tree/master" class="selected" highlight="repo_source">Source</a></li>
    <li><a href="http://github.com/faridani/PyNLP/commits/master" highlight="repo_commits">Commits</a></li>

    
    <li><a href="/faridani/PyNLP/network" highlight="repo_network">Network (1)</a></li>

    
      <li><a href="/faridani/PyNLP/forkqueue" highlight="repo_fork_queue">Fork Queue</a></li>
    

    
      
      <li><a href="/faridani/PyNLP/issues" highlight="issues">Issues (0)</a></li>
    

    
      
      <li><a href="/faridani/PyNLP/downloads">Downloads (0)</a></li>
    

          
      <li><a href="http://wiki.github.com/faridani/PyNLP/">Wiki (2)</a></li>
    
    <li><a href="/faridani/PyNLP/graphs" highlight="repo_graphs">Graphs</a></li>

    <li class="contextswitch nochoices">
      <span class="toggle leftwards" >
        <em>Branch:</em>
        <code>master</code>
      </span>
    </li>
  </ul>

  <div style="display:none" id="pl-description"><p><em class="placeholder">click here to add a description</em></p></div>
  <div style="display:none" id="pl-homepage"><p><em class="placeholder">click here to add a homepage</em></p></div>

  <div class="subnav-bar">
  
  <ul>
    <li>
      <a href="#" class="dropdown">Switch Branches (1)</a>
      <ul>
        
          
            <li><strong>master &#x2713;</strong></li>
            
      </ul>
    </li>
    <li>
      <a href="#" class="dropdown defunct">Switch Tags (0)</a>
      
    </li>
    <li>
    
    <a href="/faridani/PyNLP/branches" class="manage">Branch List</a>
    
    </li>
  </ul>
</div>

  
  
  
  
  
  



        
    <div id="repo_details" class="metabox clearfix">
      <div id="repo_details_loader" class="metabox-loader" style="display:none">Sending Request&hellip;</div>

      

      <div id="repository_description" rel="repository_description_edit">
        
          <p>... just because nltk is too heavy
            <span id="read_more" style="display:none">&mdash; <a href="#readme">Read more</a></span>
          </p>
        
      </div>
      <div id="repository_description_edit" style="display:none;" class="inline-edit">
        <form action="/faridani/PyNLP/edit/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="51a195d98d6f22525f998d49b2a520e9e3d83c74" /></div>
          <input type="hidden" name="field" value="repository_description">
          <input type="text" class="textfield" name="value" value="... just because nltk is too heavy">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      
      <div class="repository-homepage" id="repository_homepage" rel="repository_homepage_edit">
        <p><a href="http://" rel="nofollow"></a></p>
      </div>
      <div id="repository_homepage_edit" style="display:none;" class="inline-edit">
        <form action="/faridani/PyNLP/edit/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="51a195d98d6f22525f998d49b2a520e9e3d83c74" /></div>
          <input type="hidden" name="field" value="repository_homepage">
          <input type="text" class="textfield" name="value" value="">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      <div class="rule "></div>

            <div id="url_box" class="url-box">
        <ul class="clone-urls">
          
            
              <li id="private_clone_url"><a href="git@github.com:faridani/PyNLP.git" data-permissions="Read+Write">SSH</a></li>
            
            <li id="http_clone_url"><a href="https://faridani@github.com/faridani/PyNLP.git" data-permissions="Read+Write">HTTP</a></li>
            <li id="public_clone_url"><a href="git://github.com/faridani/PyNLP.git" data-permissions="Read-Only">Git Read-Only</a></li>
          
        </ul>
        <input type="text" spellcheck="false" id="url_field" class="url-field" />
              <span style="display:none" id="url_box_clippy"></span>
      <span id="clippy_tooltip_url_box_clippy" class="clippy-tooltip tooltipped" title="copy to clipboard">
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="14"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="http://assets0.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=url_box_clippy&amp;copied=&amp;copyto=">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="http://assets0.github.com/flash/clippy.swf?v5"
             width="14"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=url_box_clippy&amp;copied=&amp;copyto="
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      </span>

        <p id="url_description">This URL has <strong>Read+Write</strong> access</p>
      </div>
    </div>


        

      </div><!-- /.pagehead -->

      









<script type="text/javascript">
  GitHub.currentCommitRef = 'master'
  GitHub.currentRepoOwner = 'faridani'
  GitHub.currentRepo = "PyNLP"
  GitHub.downloadRepo = '/faridani/PyNLP/archives/master'

  
    GitHub.hasWriteAccess = true
    GitHub.hasAdminAccess = true
    GitHub.watchingRepo = true
    GitHub.ignoredRepo = false
    GitHub.hasForkOfRepo = null
    GitHub.hasForked = true
  

  
</script>










  <div id="commit">
    <div class="group">
        
  <div class="envelope commit">
    <div class="human">
      
        <div class="message"><pre><a href="/faridani/PyNLP/commit/fbae66d363000bfd692876f9ecd52dabbdc2089f">better import</a> </pre></div>
      

      <div class="actor">
        <div class="gravatar">
          
          <img src="http://www.gravatar.com/avatar/46c83b6cafe5077dfdc0cd6b818e7e4f?s=140&d=http%3A%2F%2Fgithub.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="30" height="30"  />
        </div>
        <div class="name"><a href="/faridani">faridani</a> <span>(author)</span></div>
        <div class="date">
          <abbr class="relatize" title="2010-07-20 23:24:03">Tue Jul 20 23:24:03 -0700 2010</abbr>
        </div>
      </div>

      

    </div>
    <div class="machine">
      <span>c</span>ommit&nbsp;&nbsp;<a href="/faridani/PyNLP/commit/fbae66d363000bfd692876f9ecd52dabbdc2089f" hotkey="c">fbae66d363000bfd6928</a><br />
      <span>t</span>ree&nbsp;&nbsp;&nbsp;&nbsp;<a href="/faridani/PyNLP/tree/fbae66d363000bfd692876f9ecd52dabbdc2089f/crawlers" hotkey="t">e7544510d95c5048496b</a><br />
      
        <span>p</span>arent&nbsp;
        
        <a href="/faridani/PyNLP/tree/84c784c826e50e3aad745c1834b169d5dcbd7f28/crawlers" hotkey="p">84c784c826e50e3aad74</a>
      

    </div>
  </div>

    </div>
  </div>



  
    <div id="path">
      <b><a href="/faridani/PyNLP/tree/master">PyNLP</a></b> / <a href="/faridani/PyNLP/tree/master/dataTools">dataTools</a> / importMatlabData.py       <span style="display:none" id="clippy_4531">dataTools/importMatlabData.py</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="http://assets0.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_4531&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="http://assets0.github.com/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_4531&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div id="files">
      <div class="file">
        <div class="meta">
          <div class="info">
            <span class="icon"><img alt="Txt" height="16" src="http://assets2.github.com/images/icons/txt.png?ff378e631d68c65b4c5c52a30c91c5851c1c721b" width="16" /></span>
            <span class="mode" title="File Mode">100644</span>
            
              <span>17 lines (11 sloc)</span>
            
            <span>0.315 kb</span>
          </div>
          <ul class="actions">
            
              <li><a id="file-edit-link" href="#" rel="/faridani/PyNLP/file-edit/__ref__/dataTools/importMatlabData.py">edit</a></li>
            
            <li><a href="/faridani/PyNLP/raw/master/dataTools/importMatlabData.py" id="raw-url">raw</a></li>
            
              <li><a href="/faridani/PyNLP/blame/master/dataTools/importMatlabData.py">blame</a></li>
            
            <li><a href="/faridani/PyNLP/commits/master/dataTools/importMatlabData.py">history</a></li>
          </ul>
        </div>
        
  <div class="data syntax type-python">
    
      <table cellpadding="0" cellspacing="0">
        <tr>
          <td>
            <pre class="line_numbers"><span id="LID1" rel="#L1">1</span>
<span id="LID2" rel="#L2">2</span>
<span id="LID3" rel="#L3">3</span>
<span id="LID4" rel="#L4">4</span>
<span id="LID5" rel="#L5">5</span>
<span id="LID6" rel="#L6">6</span>
<span id="LID7" rel="#L7">7</span>
<span id="LID8" rel="#L8">8</span>
<span id="LID9" rel="#L9">9</span>
<span id="LID10" rel="#L10">10</span>
<span id="LID11" rel="#L11">11</span>
<span id="LID12" rel="#L12">12</span>
<span id="LID13" rel="#L13">13</span>
<span id="LID14" rel="#L14">14</span>
<span id="LID15" rel="#L15">15</span>
<span id="LID16" rel="#L16">16</span>
<span id="LID17" rel="#L17">17</span>
</pre>
          </td>
          <td width="100%">
            
              <div class="highlight"><pre><div class='line' id='LC1'><span class="c">## This script imports Matlab data files ( .mat)</span></div><div class='line' id='LC2'><span class="c"># TODO: make it pythonic</span></div><div class='line' id='LC3'><span class="c">#       Blend it with the rest of the code</span></div><div class='line' id='LC4'><br/></div><div class='line' id='LC5'><span class="kn">import</span> <span class="nn">warnings</span></div><div class='line' id='LC6'><span class="n">warnings</span><span class="o">.</span><span class="n">filterwarnings</span><span class="p">(</span><span class="s">"ignore"</span><span class="p">)</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="kn">import</span> <span class="nn">scipy.io</span></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><br/></div><div class='line' id='LC11'><span class="k">def</span> <span class="nf">loadmat</span><span class="p">(</span><span class="n">matfile</span><span class="p">):</span></div><div class='line' id='LC12'>	<span class="c">#matfile should be without .mat	</span></div><div class='line' id='LC13'>	<span class="n">Yback</span> <span class="o">=</span> <span class="n">scipy</span><span class="o">.</span><span class="n">io</span><span class="o">.</span><span class="n">loadmat</span><span class="p">(</span><span class="n">matfile</span><span class="o">+</span><span class="s">&#39;.mat&#39;</span><span class="p">)</span></div><div class='line' id='LC14'>	<span class="n">Y</span><span class="o">=</span> <span class="n">Yback</span><span class="p">[</span><span class="n">matfile</span><span class="p">]</span></div><div class='line' id='LC15'>	<span class="k">return</span> <span class="n">Y</span></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'><br/></div></pre></div>
            
          </td>
        </tr>
      </table>
    
  </div>


      </div>
    </div>

  


    </div>
  
      

      <div class="push"></div>
    </div>

    <div id="footer">
      <div class="site">
        <div class="info">
          <div class="links">
            <a href="http://github.com/blog"><b>Blog</b></a> |
            <a href="http://support.github.com?sso=_-D9qfwBNALVWtVhGCwVCzX3G3akBoO36XQ8M-kMER3mItaw2V5DpBTBMMTZiae47ZkT-_Qqvt97Vbqqqf1_o329h7hAcMrHLKP-9HfU7k8BunVWGrJieJPf_jVENpBNjnmir_j6vyZLu24pNVBf5tFDIwjlJWT7oJzL7iNgFxfzGcuIXWbnVDNF7ay9Ny6V1Bcy9rQrzQOVQToqe0BcaSVxGbjFIJ0bprtnPlFEOHs">Support</a> |
            <a href="http://github.com/training">Training</a> |
            <a href="http://jobs.github.com">Job Board</a> |
            <a href="http://github.com/contact">Contact</a> |
            <a href="http://develop.github.com">API</a> |
            <a href="http://status.github.com">Status</a> |
            <a href="http://twitter.com/github">Twitter</a> |
            <a href="http://help.github.com">Help</a>
          </div>
          <div class="company">
            &copy;
            2010
            <span id="_rrt" title="0.31917s from fe2.rs.github.com">GitHub</span> Inc.
            All rights reserved. |
            <a href="/site/terms">Terms</a> |
            <a href="/site/privacy">Privacy</a> |
            <a href="http://github.com/security">Security</a>
          </div>
        </div>
        <div class="sponsor">
          <div>
            Powered by the <a href="http://www.rackspace.com">Dedicated
            Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
            Computing</a> of Rackspace Hosting<span>&reg;</span>
          </div>
          <a href="http://www.rackspace.com">
            <img alt="Dedicated Server" src="http://assets1.github.com/images/modules/footer/rackspace_logo.png?ff378e631d68c65b4c5c52a30c91c5851c1c721b" />
          </a>
        </div>
      </div>
    </div>

    
      
      
        <!-- current locale: en -->
        <div class="locales">
          <div class="site">
            <ul class="choices">
              
                
                  <li><span class="current">English</span></li>
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=ca">Català</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=cs">Čeština</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=de">Deutsch</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=es">Español</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=fr">Français</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=hr">Hrvatski</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=id">Indonesia</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=it">Italiano</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=ja">日本語</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=nl">Nederlands</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=no">Norsk</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=pl">Polski</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=pt-BR">Português (BR)</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=sr">Српски</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=sv">Svenska</a></li>
                  
                
              
                
                  
                    <li><a rel="nofollow" href="?locale=zh">中文</a></li>
                  
                
              
            </ul>
          </div>
        </div>
      
    

    <script>window._auth_token = "51a195d98d6f22525f998d49b2a520e9e3d83c74"</script>
    

    <script type="text/javascript">
      _kmq.push(['trackClick', 'entice_banner_link', 'Entice banner clicked']);
      
    </script>
    
  </body>
</html>

