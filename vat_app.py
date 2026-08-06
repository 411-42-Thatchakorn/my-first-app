import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
vat = price * 0.07
net_price = price - vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.divider()
st.write("นางสาวธัชกร สุทธิจำนงค์ เลขที่ 42  ม.4//11")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
