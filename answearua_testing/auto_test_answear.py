from answearua_testing.Model import answear

def test_auto():
    answear.open()
    answear.cookie_accept()
    answear.authorize()
    answear.search('кеди')
    answear.filters()
    answear.add_to_bag()
    answear.delete_from_bag()
    answear.back_to_start_page()
    answear.profile_logout()
    answear.negative_test()