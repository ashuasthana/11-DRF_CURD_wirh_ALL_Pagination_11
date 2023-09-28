==================In this drf 3 types of pagination discussed.=============================
1:PageNumberPagination
2:LimitOffsetPagination
3:CursorPagination

Note:its applicable globally and locally both.

=1==============How to send request for PageNumberPagination=================================
1:Get record as per page_size.
http://127.0.0.1:8000/api/
2:Get page 2 records.
http://127.0.0.1:8000/api/?mypage=2
3:Get 8 records per page.
http://127.0.0.1:8000/api/?num=8
4:Get page 2 per page records 8
http://127.0.0.1:8000/api/?num=8&mypage=2
5:Get 11 records per page bcouse max_page_size = 11.
http://127.0.0.1:8000/api/?num=12
6:Get last page records.
http://127.0.0.1:8000/api/?mypage=end_page
7:Get last page records as per page 10 records.
http://127.0.0.1:8000/api/?mypage=end_page&num=10

=2==============How to send request for LimitOffsetPagination=================================
1:Get record as per default_limit.
http://127.0.0.1:8000/api/
2:Get  10 records per page.
http://127.0.0.1:8000/api/?mylimit=10
3: After 5th record Get records per page
http://127.0.0.1:8000/api/?myoffset=5
4:After 5th record Get 10 records per page
http://127.0.0.1:8000/api/?myoffset=5&mylimit=10
5:After 5th record Get 11 records per page becouse max_limit is 11.
http://127.0.0.1:8000/api/?myoffset=5&mylimit=15

=3==============How to send request for CursorPagination=================================
1:Get record as per page_size and esal descending becouse ordering = '-esal'.
http://127.0.0.1:8000/api/