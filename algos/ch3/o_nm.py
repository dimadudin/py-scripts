def get_avg_brand_followers(all_handles, brand_name):
    sum = 0
    for inf in all_handles:
        for handle in inf:
            if brand_name in handle:
                sum += 1
    return sum / len(all_handles)
