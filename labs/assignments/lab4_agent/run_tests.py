from dotenv import load_dotenv
load_dotenv()

from agent import graph

TESTS = [
    ("Test 1 — Direct Answer (Không cần tool)",
     "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."),

    ("Test 2 — Single Tool Call",
     "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"),

    ("Test 3 — Multi-Step Tool Chaining",
     "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!"),

    ("Test 4 — Missing Info / Clarification",
     "Tôi muốn đặt khách sạn"),

    ("Test 5 — Guardrail / Refusal",
     "Giải giúp tôi bài tập lập trình Python về linked list"),
]

for name, user_input in TESTS:
    print("=" * 60)
    print(f"TEST: {name}")
    print(f"Bạn: {user_input}")
    print()
    print("TravelBuddy đang suy nghĩ...")
    result = graph.invoke({"messages": [("human", user_input)]})
    final = result["messages"][-1]
    print(f"TravelBuddy: {final.content}")
    print()
