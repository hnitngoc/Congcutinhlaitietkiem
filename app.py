import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Tính Lãi Tiết Kiệm", page_icon="💰", layout="centered")

def main():
    st.title("💰 Ứng dụng Tính Lãi Tiết Kiệm")
    st.markdown("Nhập các thông tin bên dưới để tính toán số tiền lãi nhận được từ khoản tiền gửi của bạn.")

    # Tạo form nhập liệu
    with st.container():
        st.subheader("📝 Thông tin gửi tiền")
        
        # Nhập số tiền gửi
        principal = st.number_input(
            "Số tiền gửi (VNĐ)", 
            min_value=0.0, 
            value=10000000.0, 
            step=1000000.0,
            format="%f"
        )
        
        # Tạo 2 cột cho kỳ hạn và lãi suất
        col1, col2 = st.columns(2)
        with col1:
            term_months = st.number_input("Kỳ hạn (Tháng)", min_value=1, value=12, step=1)
        with col2:
            interest_rate = st.number_input("Lãi suất (%/năm)", min_value=0.0, value=5.0, step=0.1)
            
        # Chọn hình thức nhận lãi
        payment_method = st.selectbox(
            "Hình thức nhận lãi", 
            ["Cuối kỳ", "Hàng tháng", "Hàng quý"]
        )

    # Nút bấm để tính toán
    if st.button("🧮 Tính Toán", type="primary"):
        # Xử lý logic tính toán cơ bản (Lãi đơn)
        # Công thức chung: Tổng lãi = Số tiền gửi * (Lãi suất / 100) * (Kỳ hạn / 12)
        total_interest = principal * (interest_rate / 100) * (term_months / 12)
        total_amount = principal + total_interest
        
        # Tính toán tiền lãi định kỳ dựa trên hình thức nhận lãi
        if payment_method == "Cuối kỳ":
            periodic_interest = total_interest
            period_label = "Tiền lãi nhận cuối kỳ"
            
        elif payment_method == "Hàng tháng":
            periodic_interest = principal * (interest_rate / 100) / 12
            period_label = "Tiền lãi nhận mỗi tháng"
            
        elif payment_method == "Hàng quý":
            # Kiểm tra xem kỳ hạn có hợp lệ cho hàng quý không
            if term_months < 3:
                st.warning("Kỳ hạn dưới 3 tháng, tiền lãi sẽ được tính theo hình thức cuối kỳ.")
                periodic_interest = total_interest
                period_label = "Tiền lãi nhận cuối kỳ"
            else:
                periodic_interest = principal * (interest_rate / 100) * (3 / 12)
                period_label = "Tiền lãi nhận mỗi quý"

        # Hiển thị kết quả
        st.divider()
        st.subheader("📊 Kết quả tính toán")
        
        # Sử dụng columns để hiển thị các số liệu (metrics)
        res_col1, res_col2 = st.columns(2)
        
        with res_col1:
            st.metric(label=period_label, value=f"{periodic_interest:,.0f} VNĐ")
            st.metric(label="Tổng số tiền gốc", value=f"{principal:,.0f} VNĐ")
            
        with res_col2:
            st.metric(label="Tổng tiền lãi", value=f"{total_interest:,.0f} VNĐ")
            st.metric(label="Tổng số tiền (Gốc + Lãi)", value=f"{total_amount:,.0f} VNĐ")

        # Hiển thị thông báo phụ nếu kỳ hạn không chia hết cho quý
        if payment_method == "Hàng quý" and term_months % 3 != 0 and term_months >= 3:
            st.info(f"Lưu ý: Kỳ hạn {term_months} tháng không chia hết cho quý (3 tháng). Số tiền lãi lẻ của các tháng cuối có thể được thanh toán vào cuối kỳ tùy theo quy định của ngân hàng.")

if __name__ == "__main__":
    main()
