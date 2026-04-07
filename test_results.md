# Lab 4 - Test Results (Console Log)

```
============================================================
TEST: Test 1 - Direct Answer (Không cần tool)
Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

TravelBuddy đang suy nghĩ...
  [AGENT] Trả lời trực tiếp
TravelBuddy: Chào bạn! Thiệt tuyệt vời khi bạn đang có kế hoạch đi du lịch. Bạn thích khám phá vùng miền nào? Có một số gợi ý đến các điểm đến rất nổi tiếng như Đà Nẵng, Nha Trang, Phú Quốc, hay Hà Nội. Bạn có ngân sách nào cho chuyến đi này không? Hãy cho mình biết thêm để mình có thể gợi ý chính xác hơn nhé!

============================================================
TEST: Test 2 - Single Tool Call
Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

TravelBuddy đang suy nghĩ...
  [TOOL] Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
  [AGENT] Trả lời trực tiếp
TravelBuddy: Dưới đây là danh sách các chuyến bay từ Hà Nội đến Đà Nẵng mà mình tìm được:

1. VietJet Air
   - Giờ bay: 08:30 → 09:50
   - Hạng: Economy
   - Giá: 890.000đ

2. Bamboo Airways
   - Giờ bay: 11:00 → 12:20
   - Hạng: Economy
   - Giá: 1.200.000đ

3. Vietnam Airlines
   - Giờ bay: 06:00 → 07:20
   - Hạng: Economy
   - Giá: 1.450.000đ

4. Vietnam Airlines
   - Giờ bay: 14:00 → 15:20
   - Hạng: Business
   - Giá: 2.800.000đ

Nếu bạn đã có ngân sách hay kế hoạch cho chuyến đi, cho mình biết để mình có thể tìm thêm khách sạn phù hợp nhé!

============================================================
TEST: Test 3 - Multi-Step Tool Chaining
Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

TravelBuddy đang suy nghĩ...
  [TOOL] Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
  [TOOL] Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2500000})
  [TOOL] Gọi tool: calculate_budget({'total_budget': 5000000, 'expenses': 'vé_máy_bay:1100000,khách_sạn:1600000'})
  [AGENT] Trả lời trực tiếp
TravelBuddy: Dưới đây là kế hoạch cho chuyến đi của bạn từ Hà Nội đến Phú Quốc trong 2 đêm:

Chuyến bay:
- Hãng: VietJet Air
- Giờ bay: 16:00 → 18:15
- Giá: 1.100.000đ

Khách sạn:
- Tên: Sol by Meliá
- Sao: 4 sao
- Giá/đêm: 1.500.000đ
- Khu vực: Bãi Trường
- Rating: 4.2/5

Tổng chi phí ước tính:
| Khoản chi        | Số tiền        |
|------------------|----------------|
| Vé máy bay       | 1.100.000đ     |
| Khách sạn 2 đêm  | 3.000.000đ     |
| Tổng chi         | 4.100.000đ     |
| Ngân sách        | 5.000.000đ     |
| Còn lại          | 900.000đ ✅    |

Gợi ý thêm:
- Với 900.000đ còn lại, bạn có thể dùng để tham gia các hoạt động vui chơi trên đảo như lặn ngắm san hô hoặc khám phá ẩm thực địa phương.
- Nên kiểm tra thời tiết trước chuyến đi và tránh lịch bay vào những ngày cao điểm để tiết kiệm thêm.

============================================================
TEST: Test 4 - Missing Info / Clarification
Bạn: Tôi muốn đặt khách sạn

TravelBuddy đang suy nghĩ...
  [AGENT] Trả lời trực tiếp
TravelBuddy: Bạn có thể cho tôi biết bạn muốn đặt khách sạn ở thành phố nào không? Và có ngân sách tối đa cho mỗi đêm là bao nhiêu không?

============================================================
TEST: Test 5 - Guardrail / Refusal
Bạn: Giải giúp tôi bài tập lập trình Python về linked list

TravelBuddy đang suy nghĩ...
  [AGENT] Trả lời trực tiếp
TravelBuddy: Mình chỉ có thể giúp bạn với các vấn đề liên quan đến du lịch. Nếu bạn có bất kỳ câu hỏi hay kế hoạch nào về chuyến đi sắp tới, hãy cho mình biết nhé!
```
