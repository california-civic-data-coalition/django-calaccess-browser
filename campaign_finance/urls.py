from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django.views.generic.base import RedirectView

from campaign_finance.api import FilerResource
from campaign_finance import views

v1_api = Api(api_name='v1')
v1_api.register(FilerResource())

urlpatterns = patterns(
    'campaign_finance.views',
    url(
        r'^$',
        views.IndexView.as_view(template_name='home/index.html'),
        name='index'
    ),
    url(r'^explore$',
        RedirectView.as_view(
            url='/explore/1/',
            permanent=True,
        ),
    ),
    url(
        r'^explore/(?P<page>[\d+]+)/$',
        views.FilerListView.as_view(template_name='filer/list.html'),
        name='filer_list'
    ),
    url(
        r'^filer/(?P<pk>\d+)/$',
        views.FilerDetailView.as_view(template_name='filer/detail.html'),
        name='filer_detail'
    ),




    ########
#
# url(r'^category/(?P<slug>[-_\w]+)/1/$',
#     RedirectView.as_view(
#         url='/category/%(slug)s/',
#         permanent=True,
#     ), name="category-list-page-1-redirect"),
#
# url(r'^category/(?P<slug>[-_\w]+)/(?P<page>[\d+]+)/$',
#     BaseCategoryDetailView.as_view(),
#     name="category-list-paginated"),
#





    # url(r'^committee/(?P<pk>\d+)/contributions/$',
    #     RedirectView.as_view(
    #         url='committee/%(pk)s/contributions/',
    #         permanent=True,
    #     ),
    #     name="committee_contribution_list_page_1_redirect"
    # ),
    # url(r'^committee/(?P<pk>\d+)/contributions/(?P<page>[\d+]+)/$',
    #     views.CommitteeContributionView.as_view(
    #         template_name='committee/contribution_list.html'
    #     ),
    #     name='committee_contribution_list_paginated',
    # ),

    # url(r'^committee/(?P<pk>\d+)/contributions$',
    #     RedirectView.as_view(
    #         url='/1',
    #         permanent=True,
    #     ),
    #     name='committee_contribution_list_redirect',
    # ),

    url(r'^committee/(?P<pk>\d+)/contributions/(?P<page>[\d+]+)/$',
        views.CommitteeContributionView.as_view(
            template_name='committee/contribution_list.html'
        ),
        name='committee_contribution_list',
    ),

    url(r'^committee/(?P<pk>\d+)/expenditures/$',
        views.CommitteeExpenditureView.as_view(
            template_name='committee/expenditure_list.html'
        ),
        name='committee_expenditure_list',
    ),
    url(
        r'^committee/(?P<pk>\d+)/$',
        (
            views.
            CommitteeDetailView
            .as_view(
                template_name='committee/detail.html'
            )
        ),
        name='committee_detail'
    ),
    url(
        r'^filing/(?P<pk>\d+)/$',
        views.FilingDetailView.as_view(template_name='filing/detail.html'),
        name='filing_detail'
    ),

    # API
    url(r'^api/', include(v1_api.urls)),

)
