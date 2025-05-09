from django.shortcuts import render
from store.models import Product, ReviewRating, Book, Provisions, Stationary,  Footwear,  Electronics,  Clothing
from category.models import BookCategory, ProvisionCategory, FootwearCategory,  ClothingCategory
import random

def home(request):
    # Fetch a few from each category
    books = list(Book.objects.filter(is_available=True)[:3])
    provisions = list(Provisions.objects.filter(is_available=True)[:3])
    stationery = list(Stationary.objects.filter(is_available=True)[:3])
    footwear = list(Footwear.objects.filter(is_available=True)[:3])
    electronics = list(Electronics.objects.filter(is_available=True)[:3])
    clothing = list(Clothing.objects.filter(is_available=True)[:3])

    mixed_products = books + provisions + stationery + footwear + electronics + clothing
    random.shuffle(mixed_products)
    featured_products = mixed_products[:12]

    
    product_ids = [product.id for product in featured_products]
    reviews = ReviewRating.objects.filter(product_id__in=product_ids, status=True)

    context = {
        'products': featured_products,
        'reviews': reviews,
        'category': 'home',
        'page_name': 'home',
    }
    return render(request, 'home.html', context)



def books(request):
    categories = BookCategory.objects.all() 
    books = Book.objects.filter(is_available=True)
    
    
    reviews_dict = {}  
    for book in books:
        reviews_dict[book.id] = ReviewRating.objects.filter(product_id=book.id, status=True)

    context = {
        'products': books,
        'categories': categories,
        'reviews': reviews_dict,  
        'category': 'books',
        'page_name': 'books',
    }
    return render(request, 'books/books.html', context)

def provisions(request):
    categories = ProvisionCategory.objects.all() 
    provisions = Provisions.objects.filter(is_available=True)

    # Get the reviews
    reviews = None
    for product in provisions:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': provisions,
        'reviews': reviews,
        'category': 'provisions',
        'page_name': 'provisions',

    }
    return render(request, 'provision/provisions.html', context)

def stationary(request):
    stationary = Stationary.objects.filter(is_available=True)

    reviews = None  
    for product in stationary:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': stationary,
        'reviews': reviews,
        'category': 'stationary',
        'page_name': 'stationary',
    }
    return render(request, 'stationary/stationary.html', context)


def footwear(request):
    categories = FootwearCategory.objects.all() 
    footwear = Footwear.objects.filter(is_available=True)

    # Get the reviews
    reviews = None
    for product in footwear:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': footwear,
        'reviews': reviews,
        'categories': categories,
        'category': 'footwear',
        'page_name': 'footwear',
    }

    return render(request, 'footwear/footwear.html', context)


def electronics(request):
    electronics = Electronics.objects.filter(is_available=True)

    # Get the reviews
    reviews = None
    for product in electronics:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': electronics,
        'reviews': reviews,
        'category': 'electronics',
        'page_name': 'electronics',
    }

    return render(request, 'electronics/electronics.html', context)


def clothing(request):
    categories = ClothingCategory.objects.all() 
    clothing = Clothing.objects.filter(is_available=True)

    # Get the reviews
    reviews = None
    for product in clothing:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': clothing,
        'reviews': reviews,
        'categories': categories,
        'category': 'clothing',
        'page_name': 'clothing',
    }

    return render(request, 'uniform/uniform.html', context)


###### Chatbot Integration

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import re

# Set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
def chatbot_reply(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            # Convert message to lowercase for easier matching
            message_lower = user_message.lower()

            # Define comprehensive knowledge base for the chatbot
            knowledge_base = {
                # Greeting responses
                "greeting": {
                    "keywords": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "greetings"],
                    "response": "Hello there! Welcome to Backtoschool. How can I help you with your school supplies today?"
                },
                
                # Books category
                "books": {
                    "keywords": ["book", "textbook", "novel", "story book", "storybook", "reading", "study guide", "workbook"],
                    "response": "We have a comprehensive collection of books including textbooks for all grade levels, storybooks, workbooks, and study guides. Our books range from GHS 15 to GHS 100 depending on the type. Would you like recommendations for a specific grade level or subject?"
                },
                
                # Uniform category
                "uniforms": {
                    "keywords": ["uniform", "school uniform", "dress", "shirt", "shorts", "skirt", "pinafore"],
                    "response": "Our uniform section offers high-quality school uniforms for all ages. We stock shirts, shorts, skirts, pinafores, and complete uniform sets. Prices range from GHS 30 to GHS 150. Do you need uniforms for a specific school or age group?"
                },
                
                # Inner wear category
                "innerwear": {
                    "keywords": ["inner", "underwear", "vest", "singlet", "undershirt", "boxer", "briefs", "panties", "socks"],
                    "response": "We provide comfortable and durable inner wear for students including vests, singlets, underwear, and socks. Our products are available in various sizes for all age groups, starting from GHS 10. What specific inner wear items are you looking for?"
                },
                
                # Footwear category
                "footwear": {
                    "keywords": ["shoe", "footwear", "sandal", "sneaker", "canvas", "boot", "sock"],
                    "response": "Our footwear collection includes school shoes, sandals, sneakers, and sports shoes suitable for school activities. We have sizes for all age groups, and prices range from GHS 50 to GHS 200. Are you looking for a specific type of school footwear?"
                },
                
                # Stationery category
                "stationery": {
                    "keywords": ["stationery", "pen", "pencil", "eraser", "ruler", "notebook", "exercise book", "crayon", "marker", "highlighter", "sharpener", "calculator"],
                    "response": "Our stationery section is fully stocked with all essential items including pens, pencils, notebooks, exercise books, erasers, rulers, calculators, and more. We have both standard and premium options, with prices starting from GHS 2. What specific stationery items do you need?"
                },
                
                # Provisions category
                "provisions": {
                    "keywords": ["provision", "food", "snack", "beverage", "drink", "milk", "chocolate", "biscuit", "cereal", "milo", "sugar", "tea"],
                    "response": "We offer a wide range of provisions for students including beverages, snacks, cereals, and other essential food items. Our provisions are carefully selected to meet nutritional needs while being convenient for school use. Prices vary based on the items. What specific provisions are you interested in?"
                },
                
                # Electronics category
                "electronics": {
                    "keywords": ["electronic", "calculator", "computer", "laptop", "tablet", "phone", "headphone", "earphone", "printer", "flash drive", "memory card"],
                    "response": "Our electronics section includes calculators, tablets, educational computers, headphones, flash drives, and other school-related electronic devices. We offer options for various budgets and educational levels. Prices range from GHS 20 for basic calculators to GHS 1500+ for laptops. What kind of electronic device are you looking for?"
                },
                
                # Dormitory essentials category
                "dormitory": {
                    "keywords": ["dormitory", "dorm", "boarding", "trunk", "chest", "suitcase", "mattress", "pillow", "bedding", "towel", "toiletry", "bucket", "mosquito net", "chop box"],
                    "response": "For boarding students, we have all dormitory essentials including trunks, chop boxes, mattresses, pillows, bedding sets, towels, toiletries, buckets, and mosquito nets. Our items are durable and specifically designed for boarding school use. Prices range from GHS 30 for basic items to GHS 300+ for trunks and mattresses. Which boarding items do you need?"
                },
                
                # Price information
                "pricing": {
                    "keywords": ["price", "cost", "how much", "expensive", "cheap", "affordable", "discount", "offer", "sale", "promotion"],
                    "response": "Our prices are competitive and vary based on the product category and quality. We offer regular discounts and special back-to-school promotions. For specific pricing, please let me know which product you're interested in. We also have bulk purchase discounts for schools and large orders."
                },
                
                # Shipping and delivery
                "delivery": {
                    "keywords": ["delivery", "shipping", "ship", "deliver", "send", "receive", "courier", "transport"],
                    "response": "We offer delivery services throughout Ghana. Delivery within Accra typically takes 1-2 business days, while delivery to other regions takes 2-5 business days. Delivery fees start from GHS 15 depending on location and order size. For bulk orders, we offer special delivery arrangements. Where would you like your order delivered?"
                },
                
                # Payment methods
                "payment": {
                    "keywords": ["payment", "pay", "mobile money", "momo", "bank transfer", "credit card", "debit card", "cash on delivery", "cod"],
                    "response": "We accept various payment methods including Mobile Money (MTN, Vodafone, AirtelTigo), bank transfers, credit/debit cards, and cash on delivery in select areas. All our payment options are secure and convenient. Which payment method would you prefer to use?"
                },
                
                # Order process
                "ordering": {
                    "keywords": ["order", "buy", "purchase", "checkout", "cart", "shopping", "shop", "how to buy", "how to order"],
                    "response": "Ordering from us is simple! Browse our website, add items to your cart, proceed to checkout, provide delivery information, choose your payment method, and confirm your order. You'll receive an order confirmation via email or SMS, and we'll update you on your delivery status. Would you like assistance with placing an order now?"
                },
                
                # Returns and refunds
                "returns": {
                    "keywords": ["return", "refund", "exchange", "damaged", "wrong", "defective", "quality issue", "cancel"],
                    "response": "We have a 7-day return policy for unopened and undamaged items. If you receive a defective product, we offer exchanges or refunds. Please contact our customer service with your order details to process any returns or exchanges. Note that custom uniform orders may have different return policies."
                },
                
                # School list assistance
                "school_list": {
                    "keywords": ["school list", "requirements", "supplies list", "shopping list", "checklist"],
                    "response": "We can help you fulfill your school supplies list! Simply send us your school's requirements, and we'll put together all the items for you. This service saves you time and ensures you get everything needed. We're familiar with the requirements of many schools in Ghana. Would you like to share your school list with us?"
                },
                
                # Special packages
                "packages": {
                    "keywords": ["package", "bundle", "set", "combo", "kit", "complete", "starter", "all in one"],
                    "response": "We offer convenient grade-specific packages that include all essential items for specific class levels. Our starter kits and bundles save you money compared to buying items individually. Popular options include our Stationery Bundle, Boarding School Kit, and Complete Class Packages. What grade or package type are you interested in?"
                },
                
                # Contact and support
                "contact": {
                    "keywords": ["contact", "help", "support", "customer service", "speak", "talk", "call", "email", "phone", "assistance", "agent", "human", "person"],
                    "response": "Our customer support team is available Monday to Saturday, 8am to 6pm. You can reach us by phone at 030-XXX-XXXX, by email at support@backtoschool.com.gh, or via WhatsApp at +233 XX XXX XXXX. Would you like me to connect you with a customer service representative?"
                },
                
                # Store locations
                "location": {
                    "keywords": ["location", "store", "shop", "branch", "physical", "visit", "address", "where", "office", "headquarter"],
                    "response": "Besides our online store, we have physical locations in Accra (East Legon and Circle), Kumasi (Adum), and Takoradi. Our stores are open Monday to Saturday, 9am to 7pm, and Sunday, 12pm to 5pm. Would you like the specific address of any of our locations?"
                },
                
                # Bulk orders and school partnerships
                "bulk_orders": {
                    "keywords": ["bulk", "wholesale", "school order", "institution", "large order", "partnership", "collaborate", "supply"],
                    "response": "We work with schools and institutions for bulk supply arrangements at wholesale rates. We offer special pricing, customized ordering, and dedicated account management for bulk orders. Many schools across Ghana partner with us for their supply needs. Please contact our business department at business@backtoschool.com.gh for more information."
                },
                
                # Age or grade specific questions
                "age_specific": {
                    "keywords": ["kindergarten", "primary", "junior high", "jhs", "senior high", "shs", "university", "college", "preschool", "nursery", "grade", "class", "form", "year"],
                    "response": "We cater to all educational levels from preschool to university. Each level has age-appropriate supplies, books, and materials. Our staff can help recommend suitable products based on age, grade level, or specific school requirements. What educational level are you shopping for?"
                },
                
                # Brand questions
                "brands": {
                    "keywords": ["brand", "quality", "best", "top", "premium", "recommended", "popular"],
                    "response": "We carry reputable local and international brands known for quality and durability. Some of our popular brands include Stedman for uniforms, BIC and Stabilo for stationery, Polo for bags, and various trusted publishers for books. We carefully select brands that offer good value while meeting school standards."
                },
                
                # Custom uniform requests
                "custom_uniforms": {
                    "keywords": ["custom uniform", "school logo", "embroidery", "tailor", "sew", "made to measure", "specific school"],
                    "response": "We offer custom uniform services with school logo embroidery and specific design requirements. For custom orders, we need your measurements and school specifications. Production typically takes 7-14 days depending on quantity. Please note that custom uniform orders require a 50% advance payment."
                },
                
                # Opening hours
                "opening_hours": {
                    "keywords": ["open", "close", "hours", "timing", "when", "schedule", "holiday", "weekend"],
                    "response": "Our online store is available 24/7. Our physical stores operate Monday to Saturday from 9am to 7pm, and Sunday from 12pm to 5pm. During back-to-school seasons (August-September and January), we extend our hours to 8am-8pm daily. Customer support is available Monday to Saturday, 8am to 6pm."
                },
                
                # Special needs supplies
                "special_needs": {
                    "keywords": ["special need", "disability", "accessible", "adaptive", "learning difficulty", "dyslexia", "adhd", "autism"],
                    "response": "We stock adaptive learning materials and supplies for students with special educational needs. These include specialized stationery, sensory items, and adapted learning tools. Our staff can guide you to appropriate resources based on specific learning needs. Please let us know the particular requirements you're looking for."
                },
                
                # Generic query
                "generic": {
                    "keywords": [],  # This will be our fallback
                    "response": "Thank you for your message! I'd be happy to help with your school supply needs. We offer books, uniforms, stationery, provisions, electronics, and dormitory essentials. Could you please provide more details about what you're looking for?"
                }
            }

            # Try to match user message to a category
            matched_response = None
            
            # First pass: Look for exact matches or strong keyword matches
            for category, data in knowledge_base.items():
                if category == "generic":  # Skip the generic fallback in first pass
                    continue
                    
                for keyword in data["keywords"]:
                    # Check for exact matches or keyword surrounded by word boundaries
                    pattern = r'\b' + re.escape(keyword) + r'\b'
                    if re.search(pattern, message_lower):
                        matched_response = data["response"]
                        logger.info(f"Matched category: {category}, keyword: {keyword}")
                        break
                
                if matched_response:
                    break
            
            # Second pass: If no strong match, look for partial matches
            if not matched_response:
                best_match = None
                highest_score = 0
                
                for category, data in knowledge_base.items():
                    if category == "generic":  # Skip the generic fallback in second pass too
                        continue
                        
                    score = 0
                    for keyword in data["keywords"]:
                        if keyword in message_lower:
                            # Longer keywords get higher scores
                            score += len(keyword)
                    
                    if score > highest_score:
                        highest_score = score
                        best_match = category
                
                if best_match and highest_score > 3:  # Minimum threshold to avoid weak matches
                    matched_response = knowledge_base[best_match]["response"]
                    logger.info(f"Partial match: {best_match}, score: {highest_score}")
            
            # If we have a match from our knowledge base, return it
            if matched_response:
                return JsonResponse({"reply": matched_response})
            
            # If no match so far, try the API call
            try:
                system_prompt = (
                    "You are a customer support assistant for 'Backtoschool', an educational e-commerce website in Ghana. "
                    "Focus exclusively on answering questions about these products and services:\n"
                    "- School supplies (books, stationery, school bags)\n"
                    "- School uniforms and inner wear\n"
                    "- Footwear for school\n"
                    "- Provisions for students\n"
                    "- Electronics for education\n"
                    "- Dormitory essentials for boarding students\n"
                    "- Delivery within Ghana (2-5 days)\n"
                    "- Ordering process and payment methods\n"
                    "- School-related items ONLY\n\n"
                    "Keep responses brief (2-3 sentences) and focused on school supplies.\n"
                    "Always encourage the customer to provide more details about what they need.\n"
                    "If asked about unrelated topics, respond: "
                    "\"I specialize in school-related products and services. "
                    "How can I assist you with school supplies today?\""
                )

                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer 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'
                }

                payload = {
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message}
                    ],
                    "temperature": 0.3,
                    "max_tokens": 150  # Limit response length
                }

                res = requests.post('https://openrouter.ai/api/v1/chat/completions', 
                                   headers=headers, 
                                   json=payload,
                                   timeout=10)
                
                if res.status_code == 200:
                    res_data = res.json()
                    bot_reply = res_data['choices'][0]['message']['content']
                    return JsonResponse({"reply": bot_reply})
                else:
                    logger.error(f"API Error: {res.status_code} - {res.text}")
                    # Use generic fallback if API fails
                    return JsonResponse({
                        "reply": knowledge_base["generic"]["response"]
                    })
                    
            except Exception as e:
                logger.error(f"API Request Error: {str(e)}")
                # Use generic fallback if API fails
                return JsonResponse({
                    "reply": knowledge_base["generic"]["response"]
                })
                
        except Exception as e:
            logger.error(f"General Error: {str(e)}")
            return JsonResponse({
                "reply": "I'm here to help with your school supply needs. Could you please try asking your question again?"
            })
    
    return JsonResponse({"reply": "How can I help you with school supplies today?"})