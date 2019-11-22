def mod_inv(a, m):
    a = a % m;
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1

if __name__ == '__main__':
    # make the user enter a prime number P
    print("[Alice] Key generation:")

    pStr = input('    enter prime number for "p" (modulo):  ')
    p = int(pStr)

    gStr = input('    enter number "1 < g < p-1" (generator):  ')
    g = int(gStr)

    aStr = input('    enter random number "a" (secret key):  ')
    a = int(aStr)

    print('    computing "B = g^a % p" (Alice\'s public key)')
    B = pow(g, a, p)  # g**a % p # pow(g, a) % p

    print('[Alice] Alice publishes the (p, g, B) as public key')
    print('   p = {}'.format(p))
    print('   g = {}'.format(g))
    print('   B = {}'.format(B))

    print("[Bob] Encryption:")
    mStr = input('   enter a message "m < p" (number for simplicity):')
    m = int(mStr)

    bStr = input('   enter a random number "1 < b < p-1" (ephermal key):')
    b = int(bStr)

    print('   compute shared key "s = B^b % p"')
    s = pow(B, b, p)

    print('   compute first ciphertext "c1 = g^b % p" (Bob\'s public key)')
    c1 = pow(g, b, p)

    print('   compute second ciphertext "c2 = (m * s) % p"')
    c2 = (m * s) % p

    print(' Bob sends the ciphertext (c1, c2) to Alice')
    print('   c1 = {}'.format(c1))
    print('   c2 = {}'.format(c2))

    print("[Alice] Decryption:")
    print("   compute shared key \"s' = c1^a % p\"")
    s_ = pow(c1, a, p)
    assert s == s_, 'failed to calculate the shared key'

    print('   compute "s^(-1)"')
    s_inv = mod_inv(s_, p)
    assert (s * s_inv) % p == 1, 'failed to calculate the inverse'

    print('    perform decryption of the ciphertext "c2"')
    m_ = (c2 * s_inv) % p

    print('[Alice] the recovered message is: {}'.format(m_))
    assert m == m_, 'decryption failed'