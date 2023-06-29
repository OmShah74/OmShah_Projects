// Multi functionality math program
#include <bits/stdc++.h>
using namespace std;
class differentiation
{
    public:
    int p,q,r,s,t,c,d,e,f,g,h,x,u;
    void polydiff()
    {
        cout<<"f(x) = p(x^d) + q(x^e) + r(x^f) + s(x^g) + t(x^h) + c\n";
        cout<<"Enter p, q, r, s, t\n";
        cin>>p>>q>>r>>s>>t;
        cout<<"Enter d, e, f, g, h, c\n";
        cin>>d>>e>>f>>g>>h>>c;
        cout<<"f'(x) = "<<p*d<<"(x^"<<d-1<<") + "<<q*e<<"(x^"<<e-1<<") + "<<r*f<<"(x^"<<f-1<<") + "<<s*g<<"(x^"<<g-1<<") + "<<t*h<<"(x^"<<h-1<<")\n";
        cout<<"Enter value of x\n";
        cin>>x;
        cout<<"f'("<<x<<") = "<<(p*d*pow(x,d-1))+(q*e*pow(x,d-1))+(r*f*pow(x,d-1))+(s*g*pow(x,d-1))+(t*h*pow(x,d-1))<<endl;
    }
    void multidiff()
    {
        cout<<"f(x) = p*(log(x)^d) + q*(sin(x)^e) + r*(cos(x)^f) + s*(tan(x)^g) + t*(sec(x)^h) + e^x + u^x\n";
        cout<<"Enter p, q, r, s, t and u\n";
        cin>>p>>q>>r>>s>>t>>u;
        cout<<"Enter d, e, f, g and h\n";
        cin>>d>>e>>f>>g>>h;
        cout<<"f'(x) = "<<p*d<<"(log(x))^"<<d-1<<"/x + "<<q*e<<"(sin(x))^"<<e-1<<"cos(x) - "<<r*f<<"(cos(x))^"<<f-1<<"sin(x) + "<<s*g<<"(tan(x))^"<<g-1<<"sec(x)^2 + "<<t*h<<"(sec(x))^"<<h-1<<"sec(x)tan(x) + e^x + "<<u<<"^xlog(x)\n";
        cout<<"Enter value of x\n";
        cin>>x;
        cout<<"f'(x) = "<<((p*d*pow(log(x),d-1))/x)+((q*e*pow(sin(x),e-1))*cos(x))-((r*f*pow(cos(x),f-1))*sin(x))+((s*g*pow(tan(x),g-1))*pow((1/cos(x)),2))+((t*h*pow((1/cos(x)),h-1))*(1/cos(x))*tan(x))+(pow((2.72),x))+(pow(u,x)*log(x));
    }
};
class integration
{
    public:
    void polyint()
    {
        int a,b,p,q,r,m,n,o;
        float f1,f2,f3,g1,g2,g3,h1,h2;
        cout<<"Integration of\n";
        cout<<"b /\n";
        cout<<"  | p(x^m)+q(x^n)+r(x^o) dx\n";
        cout<<"a /\n";
        cout<<"Enter b and a\n";
        cin>>b>>a;
        cout<<"Enter p, q and r\n";
        cin>>p>>q>>r;
        cout<<"Enter m, n and o\n";
        cin>>m>>n>>o;
        f1=p*(pow(b,m+1))/(m+1);
        f2=q*(pow(b,n+1))/(n+1);
        f3=r*(pow(b,o+1))/(o+1);
        g1=p*(pow(a,m+1))/(m+1);
        g2=q*(pow(a,n+1))/(n+1);
        g3=r*(pow(a,o+1))/(o+1);
        h1=f1+f2+f3;
        h2=g1+g2+g3;
        cout<<"The value of definite integral is\n";
        cout<<h1-h2;
    }
    void multiint()
    {
        int a,b,e,f,g,h,i,q;
        float f1,f2,f3,f4,f5,g1,g2,g3,g4,g5,d;
        cout<<"Integration of\n";
        cout<<"b /\n";
        cout<<"  |  e(cos(x)) + f(sin(x)) + g(tan-1(x)) + h(log(x)) + i(x^q) dx\n";
        cout<<"a /\n";
        cout<<"Enter b and a\n";
        cin>>b>>a;
        cout<<"Enter e, f, g, h and i\n";
        cin>>e>>f>>g>>h>>i;
        cout<<"Enter q\n";
        cin>>q;
        f1=e*(sin(b));
        f2=f*(cos(b));
        f3=g*(1/(1+(b*b)));
        f4=h/b;
        f5=i*(pow(b,q+1))/(q+1);
        g1=e*(sin(a));
        g2=f*(cos(a));
        g3=g*(1/(1+(a*a)));
        g4=h/a;
        g5=i*(pow(a,q+1))/(q+1);
        d=f1-f2+f3+f4+f5-g1+g2-g3-g4-g5;
        cout<<"The value of definite integral is\n";
        cout<<d;
    }
};
class matrix
{
    public:
       void add(int r1,int r2,int c1,int c2)
{
    if (r1==r2 && c1==c2)
    {
        int a[r1][c1],b[r1][c1];
        cout<<"Enter elements of matrix a\n";
        for (int i=0;i<r1;i++)
        {
            for (int j=0;j<c1;j++)
            {
                cin>>a[i][j];
            }
        }
        cout<<"Enter elements of matrix b\n";
        for (int i=0;i<r1;i++)
        {
            for (int j=0;j<c1;j++)
            {
                cin>>b[i][j];
            }
        }
        int c[r1][c1];
        for (int i=0;i<r1;i++)
        {
            for (int j=0;j<c1;j++)
            {
                c[i][j]=a[i][j]+b[i][j];
            }
        }
        cout<<"Addition matrix is\n";
        for (int i=0;i<r1;i++)
        {
            for (int j=0;j<c1;j++)
            {
                cout<<c[i][j]<<" ";
            }
            cout<<endl;
        }
    }
    else
        cout<<"Enter valid dimensions\n";
}
void mult(int r1,int r2,int c1,int c2)
{
    if (c1==r2)
    {
        int a[r1][c1],b[c1][c2];
        cout<<"Enter elements of matrix a\n";
        for (int i=0;i<r1;i++)
        {
            for (int j=0;j<c1;j++)
            {
                cin>>a[i][j];
            }
        }
        cout<<"Enter elements of matrix b\n";
        for (int i=0;i<c1;i++)
        {
            for (int j=0;j<c2;j++)
            {
                cin>>b[i][j];
            }
        }
        int c[r1][c2];
        for (int i=0;i<r1;i++)
        {
            for (int j=0;j<c2;j++)
            {
                c[i][j]=0;
            }
        }
        for (int i=0;i<r1;i++)
        {
            for (int j=0;j<c2;j++)
            {
                for (int k=0;k<c1;k++)
                {
                    c[i][j]+=a[i][k]*b[k][j];
                }
            }
        }
        cout<<"Multiplication matrix is\n";
        for (int i=0;i<r1;i++)
        {
            for (int j=0;j<c2;j++)
            {
                cout<<c[i][j]<<" ";
            }
            cout<<endl;
        }
    }
    else
        cout<<"Enter valid dimensions\n";
}
void trans(int r,int c)
{
    int a[r][c],b[c][r];
    cout<<"Enter elements of matrix\n";
    for (int i=0;i<r;i++)
    {
        for (int j=0;j<c;j++)
        {
            cin>>a[i][j];
        }
    }
    for (int i=0;i<c;i++)
    {
        for (int j=0;j<r;j++)
        {
            b[i][j]=a[j][i];
        }
    }
    cout<<"Transpose of the matrix is\n";
    for (int i=0;i<c;i++)
    {
        for (int j=0;j<r;j++)
        {
            cout<<b[i][j]<<" ";
        }
        cout<<endl;
    }
} 
       void mainfn()
       { 
        int c;
        cout<<"Enter choice to perform\n1. Addition\n2. Multiplication\n3. Transpose    of matrices\n";
        cin>>c;
        switch (c)
        {
        case 1:
            {
                int r1,c1,r2,c2;
                cout<<"Enter no. of rows and columns of matrix a and b\n";
                cin>>r1>>c1>>r2>>c2;
                add(r1,r2,c1,c2);
                break;
            }
        case 2:
            {
                int r1,r2,c1,c2;
                cout<<"Enter no. of rows and columns of matrix a and b\n";
                cin>>r1>>c1>>r2>>c2;
                mult(r1,r2,c1,c2);
                break;
            }
        case 3:
            {
                int r,c;
                cout<<"Enter no. of rows and columns of matrix\n";
                cin>>r>>c;
                trans(r,c);
                break;
            }   
            }
                 }
};
class vect
{
    public:
    int x1,x2,x3,y1,y2,y3;
    void vecmath()
    {
        cout<<"Given 2 vectors v1 = x1i + x2j + x3k and v1 = x1i + x2j + x3k\n";
        cout<<"Enter coefficients of vector 1\n";
        cin>>x1>>x2>>x3;
        cout<<"Enter coefficients of vector 2\n";
        cin>>y1>>y2>>y3;
        cout<<"v1 + v2 = "<<x1+y1<<"i + "<<x2+y2<<"j + "<<x3+y3<<"k\n";
        cout<<"v1 - v2 = "<<x1-y1<<"i + "<<x2-y2<<"j + "<<x3-y3<<"k\n";
        cout<<"v1 . v2 = "<<(x1*y1)+(x2*y2)+(x3*y3)<<endl;
        cout<<"v1 x v2 = "<<(x2*y3)-(x3*y2)<<"i - "<<(x1*y3)-(x3*y1)<<"j + "<<(x1*y2)-(x2*y1)<<"k\n";
        cout<<"Unit vector v1^ = "<<(x1/sqrt((x1*x1)+(x2*x2)+(x3*x3)))<<"i + "<<(x2/sqrt((x1*x1)+(x2*x2)+(x3*x3)))<<"j + "<<(x3/sqrt((x1*x1)+(x2*x2)+(x3*x3)))<<"k\n";
        cout<<"Unit vector v2^ = "<<(y1/sqrt((y1*y1)+(y2*y2)+(y3*y3)))<<"i + "<<(y2/sqrt((y1*y1)+(y2*y2)+(y3*y3)))<<"j + "<<(y3/sqrt((y1*y1)+(y2*y2)+(y3*y3)))<<"k\n";
        cout<<"Projection of\n1. v1 along v2 = "<<((x1*y1)+(x2*y2)+(x3*y3))/sqrt((y1*y1)+(y2*y2)+(y3*y3))<<endl;
        cout<<"2. v2 along v1 = "<<((x1*y1)+(x2*y2)+(x3*y3))/sqrt((x1*x1)+(x2*x2)+(x3*x3))<<endl;
    }
};
class quadratic
{
    public:
    int a,b,c,d,e,f;
    void quadeqn()
    {
        cout<<"Quadratic equation of form \na(x^2) + bx + c = 0\n";
        cout<<"Enter a, b and c\n";
        cin>>a>>b>>c;
        d=(b*b)-4*a*c;
        if (d>=0)
        {
            e=((-b)+sqrt(d))/(2*a);
            f=((-b)-sqrt(d))/(2*a);
            cout<<"The roots of quadratic equation "<<a<<"(x^2) + "<<b<<"x + "<<c<<" = 0 is\n";
            cout<<"x = "<<e<<endl;
            cout<<"x = "<<f;
        }
        else
        {
            cout<<"The quadratic equation has imaginary roots\n";
        }
    }
};
class statistics
{
    public:
    float men1,men2,men3,med1,med2,med3;
    void AMud()
    {
        int n,s=0;
        cout<<"Enter number of observations\n";
        cin>>n;
        int ud[n];
        cout<<"Enter observations\n";
        for (int i=0;i<n;i++)
        {
            cin>>ud[i];
        }
        for (int i=0;i<n;i++)
        {
            s+=ud[i];
        }
        men1=s/n;
        cout<<"Arithmetic mean of unclassified data = "<<s/n<<endl;
    }
    void AMdf()
    {
        int n;
        cout<<"Enter number of observations\n";
        cin>>n;
        float df[n][2],s=0,t=0;
        cout<<"Enter observations and their corresponding frequencies\nxi fi\n";
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<2;j++)
            {
                cin>>df[i][j];
            }
        }
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<1;j++)
            {
                s+=(df[i][j])*(df[i][j+1]);
            }
        }
        for (int i=0;i<n;i++)
        {
            t+=df[i][1];
        }
        men2=s/t;
        cout<<"Arithmetic mean of discrete frequency distribution = "<<s/t<<endl;
    }
    void AMcfd()
    {
        int n;
        cout<<"Enter number of observations\n";
        cin>>n;
        float c[n][2],f[n],m[n],u[n],s=0,t=0;
        cout<<"Enter class interval\n";
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<2;j++)
            {
                cin>>c[i][j];
            }
        }
        cout<<"Enter corresponding frequencies\n";
        for (int i=0;i<n;i++)
        {
            cin>>f[i];
        }
        for (int i=0;i<n;i++)
        {
            m[i]=(c[i][1]+c[i][0])/2;
        }
        for (int i=0;i<n;i++)
        {
            u[i]=(m[i]-m[0])/(c[0][1]-c[0][0]);
        }
        for (int i=0;i<n;i++)
        {
            s+=f[i];
        }
        for (int i=0;i<n;i++)
        {
            t+=(f[i]*u[i]);
        }
        men3=m[0]+(((c[0][1]-c[0][0])*t)/s);
        cout<<"Mean = "<<m[0]+(((c[0][1]-c[0][0])*t)/s)<<endl;
    }
     void Mud()
    {
        int n;
        cout<<"Enter number of observations\n";
        cin>>n;
        float ud[n];
        cout<<"Enter observations\n";
        for (int i=0;i<n;i++)
        {
            cin>>ud[i];
        }
        for (int i=0;i<n-1;i++)
        {
            for (int j=i+1;j<n;j++)
            {
                if (ud[j]<ud[i])
                {
                    float t=ud[j];
                    ud[j]=ud[i];
                    ud[i]=t;
                }
            }
        }
        if (n%2==0)
        {
            med1=(ud[n/2]+ud[(n/2)+1])/2;
            cout<<"Median = "<<(ud[n/2]+ud[(n/2)+1])/2<<endl;
        }
        else if (n%2!=0)
        {
            med1=ud[(n+1)/2];
            cout<<"Median = "<<ud[(n+1)/2]<<endl;
        }
    }
    void Mdf()
    {
        int n;
        cout<<"Enter number of observations\n";
        cin>>n;
        float df[n][2],cf[n],s=0,t=0;
        cout<<"Enter observations and their corresponding frequencies\nxi fi\n";
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<2;j++)
            {
                cin>>df[i][j];
            }
        }
        for (int i=0;i<n;i++)
        {
            cf[i]=s+df[i][1];
            s+=df[i][1];
        }
        for (int i=0;i<n;i++)
        {
            t+=df[i][1];
        }
        for (int i=0;i<n-1;i++)
        {
            if ((t/2)>cf[i] && (t/2)<cf[i+1])
            {
                med2=df[i+1][0];
                cout<<"Median = "<<df[i+1][0]<<endl;
            }
        }
    }
    void Mcfd()
    {
        int n;
        cout<<"Enter number of observations\n";
        cin>>n;
        float cif[n][3],cf[n],s=0,t=0,f,l,h,F;
        cout<<"Enter class intervals and their corresponding frequencies\nci      fi\n";
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<3;j++)
            {
                cin>>cif[i][j];
            }
        }
        h=(cif[0][1]-cif[0][0]);
        for (int i=0;i<n;i++)
        {
            cf[i]=s+cif[i][2];
            s+=cif[i][2];
        }
        for (int i=0;i<n;i++)
        {
            t+=cif[i][2];
        }
        for (int i=0;i<n;i++)
        {
            if (cf[i]>(t/2))
            {
                l=cif[i][0];
                f=cif[i][2];
                F=cf[i-1];
                break;
            }
        }
        med3=l+((((t/2)-F)/f)*h);
        cout<<"Median = "<<l+((((t/2)-F)/f)*h)<<endl;
    }
};
int main()
{
    system("CLS");
    differentiation a;
    integration b;
    matrix c;
    vect d;
    quadratic e;
    statistics f;
    int s;
    do 
    {
    cout<<"\nEnter choice to perform\n1. Differentiation\n2. Integration\n3. Matrix operation\n4. Vector math\n5. Quadratic equation\n6. Statistics\n7. Exit\n";
    cin>>s;
    switch (s)
    {
        case 1:
        {
            int s1;
            cout<<"1. Polynomial dfferentiation\n2. Multi-expression differentiation\n";
            cin>>s1;
            switch (s1)
            {
                case 1:
                {
                    a.polydiff();
                    break;
                }
                case 2:
                {
                    a.multidiff();
                    break;
                }
            }
            break;
        }
        case 2:
        {
            int s2;
            cout<<"1. Polynomial integration\n2. Multi-expression integration\n";
            cin>>s2;
            switch (s2)
            {
                case 1:
                {
                    b.polyint();
                    break;
                }
                case 2:
                {
                    b.multiint();
                    break;
                }
            }
            break;
        }
        case 3:
        {
            c.mainfn();
            break;
        }
        case 4:
        {
            d.vecmath();
            break;
        }
        case 5:
        {
            e.quadeqn();
            break;
        }
        case 6:
        {
            int c;
            cout<<"1. Mean\n2. Median\n3. Mode\n";
            cin>>c;
            switch (c)
            {
                case 1:
                {
                    int c1;
                    cout<<"1. Ungrouped data\n2. Discrete frequency data\n3. Grouped data\n";
                    cin>>c1;
                    switch (c1)
                    {
                        case 1:
                        {
                            f.AMud();
                            break;
                        }
                        case 2:
                        {
                            f.AMdf();
                            break;
                        }
                        case 3:
                        {
                            f.AMcfd();
                            break;
                        }
                    }
                    break;
                }
                case 2:
                {
                    int c2;
                    cout<<"1. Ungrouped data\n2. Discrete frequency data\n3. Grouped data\n";
                    cin>>c2;
                    switch (c2)
                    {
                        case 1:
                        {
                            f.Mud();
                            break;
                        }
                        case 2:
                        {
                            f.Mdf();
                            break;
                        }
                        case 3:
                        {
                            f.Mcfd();
                            break;
                        }
                    }
                    break;
                }
                case 3:
                {
                    int c2;
                    cout<<"1. Ungrouped data\n2. Discrete frequency data\n3. Grouped data\n";
                    cin>>c2;
                    switch (c2)
                    {
                        case 1:
                        {
                            f.Mud();
                            f.AMud();
                            float mode1=(3*f.med1)-(2*f.men1);
                            cout<<"Mode = "<<mode1<<endl;
                            break;
                        }
                        case 2:
                        {
                            f.Mdf();
                            f.AMdf();
                            float mode2=(3*f.med2)-(2*f.men2);
                            cout<<"Mode = "<<mode2<<endl;
                            break;
                        }
                        case 3:
                        {
                            f.Mcfd();
                            f.AMcfd();
                            float mode3=(3*f.med3)-(2*f.men3);
                            cout<<"Mode = "<<mode3<<endl;
                            break;
                        }
                    }
                    break;
                }
            }
        }
    }
    } while (s!=7);
}