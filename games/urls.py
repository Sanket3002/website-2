from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView
from games.views import (GameList, GameListByYear,
                         GameListByGenre, GameListByPlatform)


urlpatterns = patterns(
    'games.views',
    url(r'^$', GameList.as_view(),
        name='game_list'),
    url(r'^year/(\d+)/$', GameListByYear.as_view(),
        name='games_by_year'),
    url(r'^genre/([\w-]+)/$', GameListByGenre.as_view(),
        name='games_by_genre'),
    url(r'^runner/(?P<runner_slug>[\w\-]+)$', 'games_by_runner'),
    #url(r'^developer/(?P<developer_slug>[\w\-]+)$', views.games_by_developer),
    #url(r'^publisher/(?P<publihser_slug>[\w\-]+)$', views.games_by_publisher),
    url(r'^platform/(?P<slug>[\w\-]+)$', GameListByPlatform.as_view(),
        name="games_by_plaform"),
    url(r'^add-game', 'submit_game',
        name='submit_game'),
    url(r'^game-submitted',
        TemplateView.as_view(template_name='games/submitted.html'),
        name="game-submitted"),
    url(r'install/(?P<slug>[\w\-]+).yml', 'serve_installer',
        name='serve_installer'),
    url(r'install/(?P<slug>[\w\-]+).jpg', 'serve_installer_banner',
        name='serve_installer_banner'),
    url(r'install/icon/(?P<slug>[\w\-]+).jpg', 'serve_installer_icon',
        name='serve_installer_icon'),
    url(r'(?P<slug>[\w\-]+)/installer/new$', "new_installer",
        name="new_installer"),
    url(r'(?P<slug>[\w\-]+)/installer/edit$', 'edit_installer',
        name='edit_installer'),
    url(r'(?P<slug>[\w\-]+)/installer/complete/$', 'installer_complete',
        name='installer_complete'),
    url(r'([\w\-]+)/screenshot/add/', 'screenshot_add',
        name='screenshot_add'),
    url(r'download/?', 'download_latest',
        name='download_latest'),
    url(r'^library/(?P<username>[\w-]+)/$', 'library_show',
        name="library_show"),
    url(r'^library/add/(?P<slug>[\w-]+)/$', 'library_add',
        name="add_to_library"),
    url(r'^library/remove/(?P<slug>[\w-]+)/$', 'library_remove',
        name="remove_from_library"),
    url(r'(?P<slug>[\w\-]+)/$', "game_detail",
        name="game_detail"),
)
