Xin chao minh la Thanh Tung - tunghocdata
Đây là một dự án cá nhân, mình đang tự thực hiện để học về DATA dưới sự giúp đỡ của một vài người anh chị !

Mục tiêu : Đánh giá xem công ty nào là công ty sẽ là phù hợp để mình liên hệ làm đối tác
Tiêu chí : 
- Công ty đó đang tuyển các vị trí engineer không.
- Công ty đó được funding gần đây không.
- Công ty đó đợt này có đi các event để kiếm đối tác không.
- Công ty đó có thích oursouce không (Có thể đánh giá bằng các dự án đã cũ)
- Công ty to hay nhỏ( đánh giá bằng số nhân viên, 1-200 người là ổn)

Các bước thực hiện :
B1:    Mở file backup.sql bằng sql                        
B2:    Query để ghép data (tên công ty, các job họ tuyển, size của công ty, funding của họ, lần funding gần nhất)                            
B3:     Xuất dữ liệu từ Query sql bằng file csv rồi dùng python scoring            
B4:     Scoring bằng Python (chọn ra 5 công ty tuyển nhiều job nhất, 5 công ty có funding cao nhất, 5 công ty có funding gần đây)                            
B5:     Dùng gg sheets liệt kê lại kết quả của python rồi sau đó tiến hành lọc tay        
NOTE:    Khi Query ghép data nếu thêm data đi events (không tìm đc Foreign Key và ghép xong thì không còn công ty nào)
